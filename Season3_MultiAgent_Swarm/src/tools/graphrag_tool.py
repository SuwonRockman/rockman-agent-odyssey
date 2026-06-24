import os
from langchain_core.tools import tool

# Placeholder for actual Neo4j GraphRAG implementation.
# In a full production setup, this would use LangChain's Neo4jGraph and CypherQA.
# For Phase 2, we simulate the retrieval from the local text manual to avoid immediate Neo4j dependency.

MANUAL_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'cnc_manual.txt')

@tool
def search_maintenance_manual(query: str) -> str:
    """
    Searches the equipment maintenance manuals and GraphRAG knowledge base for troubleshooting steps.
    Args:
        query (str): The symptom or error code to search for (e.g., 'high torque', 'E-01', 'overheating').
    Returns:
        Relevant troubleshooting steps and required replacement parts.
    """
    try:
        # For this prototype, we do a simple keyword search in the text manual.
        # In Phase 3, this will be replaced with a live Neo4j Cypher query.
        with open(MANUAL_PATH, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        results = []
        query_lower = query.lower()
        
        # Simple heuristic to find matching error codes or actions
        for line in lines:
            if query_lower in line.lower():
                results.append(line.strip())
                
        # Also check if it maps to known sensor anomalies
        if "torque" in query_lower or "overstrain" in query_lower:
            results.append("Detected possible Overstrain Failure (OSF) due to high torque.")
            results.append("Action: Check tool gripper and spindle for jams. Replacement part may be required: 'tool_gripper_assembly'.")
            
        if results:
            report = "📘 GraphRAG Manual Search Results:\n"
            for r in results:
                report += f"- {r}\n"
            return report
        else:
            return f"No specific troubleshooting steps found in the manual for query: '{query}'."
            
    except Exception as e:
        return f"Error accessing manual: {str(e)}"

# For testing
if __name__ == "__main__":
    print(search_maintenance_manual.invoke({"query": "torque"}))
