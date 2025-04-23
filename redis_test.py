from upstash_redis import Redis
from dotenv import load_dotenv
import os

load_dotenv()

redis = Redis(
    url=os.getenv("UPSTASH_REDIS_REST_URL"),
    token=os.getenv("UPSTASH_REDIS_REST_TOKEN"),
)

redis.set("foo", "bar")
value = redis.get("foo")
print(value)  # Output: b'bar'
