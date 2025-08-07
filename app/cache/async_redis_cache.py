import os
import redis.asyncio as aioredis
import json

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_DB = int(os.getenv("REDIS_DB", 0))

_redis = None

async def get_redis():
    global _redis
    if _redis is None:
        _redis = await aioredis.from_url(
            f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}", encoding="utf8", decode_responses=True
        )
    return _redis

async def get_cached_result(key):
    redis = await get_redis()
    value = await redis.get(key)
    if value:
        return json.loads(value)
    return None

async def set_cached_result(key, result, expire=3600):
    redis = await get_redis()
    await redis.set(key, json.dumps(result), ex=expire)