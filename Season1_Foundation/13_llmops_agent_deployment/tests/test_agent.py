import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "service": "llmops-agent-deployment"}

def test_analyze_data():
    response = client.post(
        "/api/v1/analyze",
        json={"query": "엔진 1번 온도 그래프 그려줘"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "insights" in data
