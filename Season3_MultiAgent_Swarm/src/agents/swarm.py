import os
import sqlite3
import operator
from typing import Annotated, Sequence, TypedDict, List
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode

# [Edge 3] State Memory import
from langgraph.checkpoint.sqlite import SqliteSaver

# Import tools
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from tools.monitor_tool import check_sensor_anomalies
from tools.graphrag_tool import search_maintenance_manual
from tools.sql_tool import check_inventory, create_purchase_order

# 1. Define State
class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]
    next: str

# 2. Define Supervisor Router
def create_supervisor(llm, members: List[str]):
    system_prompt = (
        "You are a Supervisor in an Autonomous Smart Factory Command Center.\n"
        "Your job is to route the conversation to the correct worker based on the situation.\n"
        f"Workers: {', '.join(members)}.\n"
        "- Route to 'Monitor' for checking factory status.\n"
        "- Route to 'Engineer' to find troubleshooting steps or parts in the manual.\n"
        "- Route to 'SupplyChain' to check part inventory or place orders.\n"
        "\n[Edge 2: Self-Correction Logic]\n"
        "- If SupplyChain reports that a part does NOT exist in the database, DO NOT finish. Route BACK to 'Engineer' to find an alternative compatible part.\n"
        "If the problem is fully resolved and required actions are taken, reply with 'FINISH'."
    )
    
    options = members + ["FINISH"]
    function_def = {
        "name": "route",
        "description": "Select the next role.",
        "parameters": {
            "type": "object",
            "properties": {"next": {"type": "string", "enum": options}},
            "required": ["next"],
        },
    }
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="messages"),
        ("system", "Given the conversation above, who should act next? Select one of: {options}")
    ]).partial(options=str(options), members=", ".join(members))

    return prompt | llm.with_structured_output(function_def)

# 3. Define Worker Node Generator
def create_agent(llm, tools, system_prompt):
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="messages"),
    ])
    return prompt | llm.bind_tools(tools)

# 4. Build the Graph
def build_swarm_graph(api_key: str):
    llm = ChatOpenAI(model="gpt-4o", temperature=0, openai_api_key=api_key)

    monitor_agent = create_agent(
        llm, [check_sensor_anomalies], 
        "You are the Monitor Agent. Check factory sensors and report anomalies concisely."
    )
    
    engineer_agent = create_agent(
        llm, [search_maintenance_manual], 
        "You are the Engineer Agent. Use the manual to find solutions and replacement parts. If a part is out of stock or invalid, find an alternative."
    )
    
    supply_chain_agent = create_agent(
        llm, [check_inventory, create_purchase_order], 
        "You are the Supply Chain Agent. Check inventory for parts. If stock is 0, issue a purchase order. If a part name is invalid, explicitly state it is not found."
    )

    def agent_node(state, agent, name):
        result = agent.invoke(state)
        if not isinstance(result, ToolMessage):
            result = AIMessage(**result.dict(exclude={"type", "name"}), name=name)
        return {"messages": [result]}

    workflow = StateGraph(AgentState)
    
    workflow.add_node("Monitor", lambda state: agent_node(state, monitor_agent, "Monitor"))
    workflow.add_node("Engineer", lambda state: agent_node(state, engineer_agent, "Engineer"))
    workflow.add_node("SupplyChain", lambda state: agent_node(state, supply_chain_agent, "SupplyChain"))
    
    workflow.add_node("Monitor_Tools", ToolNode([check_sensor_anomalies]))
    workflow.add_node("Engineer_Tools", ToolNode([search_maintenance_manual]))
    workflow.add_node("SupplyChain_Tools", ToolNode([check_inventory, create_purchase_order]))
    
    members = ["Monitor", "Engineer", "SupplyChain"]
    supervisor = create_supervisor(llm, members)
    
    def supervisor_node(state):
        res = supervisor.invoke(state)
        if isinstance(res, dict):
            next_worker = res.get("next", "FINISH")
        else:
            next_worker = "FINISH"
        return {"next": next_worker}
        
    workflow.add_node("Supervisor", supervisor_node)
    
    workflow.add_edge("Monitor_Tools", "Monitor")
    workflow.add_edge("Engineer_Tools", "Engineer")
    workflow.add_edge("SupplyChain_Tools", "SupplyChain")
    
    def router_monitor(state):
        return "Monitor_Tools" if state["messages"][-1].tool_calls else "Supervisor"
        
    def router_engineer(state):
        return "Engineer_Tools" if state["messages"][-1].tool_calls else "Supervisor"
        
    def router_supplychain(state):
        return "SupplyChain_Tools" if state["messages"][-1].tool_calls else "Supervisor"
        
    workflow.add_conditional_edges("Monitor", router_monitor, {"Monitor_Tools": "Monitor_Tools", "Supervisor": "Supervisor"})
    workflow.add_conditional_edges("Engineer", router_engineer, {"Engineer_Tools": "Engineer_Tools", "Supervisor": "Supervisor"})
    workflow.add_conditional_edges("SupplyChain", router_supplychain, {"SupplyChain_Tools": "SupplyChain_Tools", "Supervisor": "Supervisor"})
    
    workflow.add_conditional_edges("Supervisor", lambda x: x["next"], {
        "Monitor": "Monitor", "Engineer": "Engineer", "SupplyChain": "SupplyChain", "FINISH": END
    })
    
    workflow.set_entry_point("Supervisor")
    
    # [Edge 3] Attach Memory Checkpointer
    db_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'checkpoints.sqlite')
    conn = sqlite3.connect(db_path, check_same_thread=False)
    memory = SqliteSaver(conn)
    
    # [Edge 1] Human-in-the-loop interruption before SupplyChain tools execute!
    return workflow.compile(checkpointer=memory, interrupt_before=["SupplyChain_Tools"])
