from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv

from agent import agent
from agents import Runner, set_tracing_disabled
from redis_saver import RedisSaver
from upstash_redis import Redis

load_dotenv()
set_tracing_disabled(True)

# Redis client setup
redis_client = Redis(
    url=os.getenv("UPSTASH_REDIS_REST_URL"),
    token=os.getenv("UPSTASH_REDIS_REST_TOKEN")
)
saver = RedisSaver(redis_client)

app = FastAPI(title="Nova Store Assistant 🤖")

# memory_key = "nova-agent-memory"


class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
async def chat_with_agent(req: ChatRequest):
    user_input = req.message.strip()

    # Load memory (currently not used if agent doesn't support it yet)
    # memory = await saver.load_memory(memory_key)

    # Run agent
    result = await Runner.run(agent, user_input)

    # Save memory if supported
    # memory = result.chat_history
    # await saver.save_memory(memory_key, memory)

    return {"response": result.final_output}
