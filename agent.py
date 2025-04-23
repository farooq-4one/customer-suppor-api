# agent.py
import os
from dotenv import load_dotenv
from agents import Agent, OpenAIChatCompletionsModel
from openai import AsyncOpenAI
from tools import (
    fetch_all_billboards,
    fetch_billboard_by_id,
    create_billboard,
    update_billboard,
    delete_billboard
)

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure the Gemini client
gemini_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Define the agent
agent = Agent(
    name="Nova Store Assistant",
    instructions=(
        "You are Nova Store, a friendly assistant for the Store platform. "
        "You can fetch and provide information about billboards. "
        "Respond in a conversational manner, avoiding lists unless requested."
    ),
    model=OpenAIChatCompletionsModel(
        model="gemini-1.5-flash",
        openai_client=gemini_client
    ),
    tools=[
        fetch_all_billboards,
        fetch_billboard_by_id,
        create_billboard,
        update_billboard,
        delete_billboard
    ],
)
