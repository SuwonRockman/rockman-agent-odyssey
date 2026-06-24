import os
import sys
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

sys.path.append(os.path.join(os.path.dirname(__file__)))
from agents.swarm import build_swarm_graph

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    print("="*70)
    print("🏭 Autonomous AX Command Center Simulation (Advanced Edges)")
    print("="*70)
    
    env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
    load_dotenv(env_path)
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key or api_key == "your_openai_api_key_here":
        print("\n⚠️ WARNING: Please insert a valid OPENAI_API_KEY in .env")
        return

    graph = build_swarm_graph(api_key)
    
    # [Edge 3] State Memory Configuration (Thread ID remembers history)
    thread_config = {"configurable": {"thread_id": "factory_shift_001"}}
    
    print("\n[System] Memory loaded for shift 'factory_shift_001'.")
    print("[System] Initiating Swarm logic...\n")
    
    inputs = {
        "messages": [HumanMessage(content="Start the morning shift. The Machine #2 torque sensor is acting up. Check it.")]
    }
    
    # We use a while loop because the graph might hit an [Edge 1] Interrupt
    for output in graph.stream(inputs, thread_config, stream_mode="values"):
        last_msg = output["messages"][-1]
        
        # Determine who sent this
        sender = last_msg.name if getattr(last_msg, 'name', None) else "System"
        
        if isinstance(last_msg, HumanMessage):
            print(f"👤 [User] {last_msg.content}")
        elif last_msg.content:
            print(f"🤖 [{sender}] {last_msg.content}")
        elif hasattr(last_msg, 'tool_calls') and last_msg.tool_calls:
            print(f"🛠️ [{sender}] is preparing to run tool: {last_msg.tool_calls[0]['name']}...")
            
    # Check if we hit an interrupt
    state = graph.get_state(thread_config)
    if state.next and "SupplyChain_Tools" in state.next:
        print("\n" + "="*50)
        print("🚨 [Edge 1: Human-in-the-Loop] Execution Paused!")
        print("SupplyChain Agent is attempting to access the database or issue a purchase order.")
        print("="*50)
        
        user_input = input("👨‍💼 Manager, do you APPROVE this action? (Y/N): ")
        
        if user_input.strip().lower() == 'y':
            print("\n✅ Approval granted. Resuming Swarm execution...\n")
            # Resume graph with None input
            for output in graph.stream(None, thread_config, stream_mode="values"):
                last_msg = output["messages"][-1]
                sender = last_msg.name if getattr(last_msg, 'name', None) else "System"
                if last_msg.content and sender != "System":
                    print(f"🤖 [{sender}] {last_msg.content}")
        else:
            print("\n❌ Approval denied. Halting execution for safety.")
            
    print("\n🏁 [System] Shift operations completed.")

if __name__ == "__main__":
    main()
