import pickle


class RedisSaver:
    def __init__(self, redis_client):
        self.redis_client = redis_client

    async def load_memory(self, key):
        """Load memory from Redis"""
        memory = self.redis_client.get(key)
        if memory:
            return pickle.loads(memory)
        return {}

    async def save_memory(self, key, memory):
        """Save memory to Redis"""
        serialized_memory = pickle.dumps(memory)
        self.redis_client.set(key, serialized_memory)
