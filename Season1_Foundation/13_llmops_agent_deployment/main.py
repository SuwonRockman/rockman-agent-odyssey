from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent_core import DataAnalystAgent
from logger import logger

app = FastAPI(
    title="LLMOps Enterprise Agent API",
    description="Production-ready FastAPI server for the AX Data Analyst Agent.",
    version="1.0.0"
)

agent = DataAnalystAgent()

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    status: str
    query: str
    sql_executed: str
    insights: str

@app.get("/health")
async def health_check():
    """Kubernetes / Docker health check endpoint."""
    return {"status": "healthy", "service": "llmops-agent-deployment"}

@app.post("/api/v1/analyze", response_model=QueryResponse)
async def analyze_data(request: QueryRequest):
    """
    Main endpoint for the frontend or other microservices to request data analysis.
    """
    try:
        result = await agent.analyze_query(request.query)
        return result
    except Exception as e:
        logger.error("API /api/v1/analyze failed", extra={"extra_info": {"error": str(e)}})
        raise HTTPException(status_code=500, detail="Internal Agent Error")
