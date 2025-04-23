from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv

from agent import agent
from agents import Runner, set_tracing_disabled
from upstash_redis import Redis

load_dotenv()
set_tracing_disabled(True)

redis_client = Redis(
    url=os.getenv("UPSTASH_REDIS_REST_URL"),
    token=os.getenv("UPSTASH_REDIS_REST_TOKEN")
)

app = FastAPI(title="Nova Store Assistant 🤖")


class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
async def chat_with_agent(req: ChatRequest):
    user_input = req.message.strip()

    result = await Runner.run(agent, user_input)

    return {"response": result.final_output}
