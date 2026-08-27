from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

load_dotenv()

from agent import run_agent


app = FastAPI(
    title="AI Agent Demo",
    description="AI agent with LLM tool calling",
    version="1.0.0"
)


class AgentRequest(BaseModel):
    message: str


class AgentResponse(BaseModel):
    response: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/agent", response_model=AgentResponse)
def agent(request: AgentRequest):
    response = run_agent(request.message)

    return {
        "response": response
    }
