from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

from agent import agent
from agents import Runner, set_tracing_disabled

load_dotenv()
set_tracing_disabled(True)

app = FastAPI(title="Nova Store Assistant 🤖")

# Allow requests from your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
async def chat_with_agent(req: ChatRequest):
    user_input = req.message.strip()
    result = await Runner.run(agent, user_input)
    return {"response": result.final_output}
