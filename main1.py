import asyncio
from upstash_redis import Redis
from dotenv import load_dotenv
import os

from agent import agent
from agents import Runner, set_tracing_disabled

load_dotenv()
set_tracing_disabled(True)

redis_client = Redis(
    url=os.getenv("UPSTASH_REDIS_REST_URL"),
    token=os.getenv("UPSTASH_REDIS_REST_TOKEN")
)


async def main():
    print("Nova Store: Hi there! I'm Nova Store, your friendly assistant. 🤖")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"exit", "stop", "goodbye", "quit"}:
            print("Nova Store: Goodbye! 👋")
            break

        result = await Runner.run(agent, user_input)

        print(f"Nova Store: {result.final_output}\n")


if __name__ == "__main__":
    asyncio.run(main())
