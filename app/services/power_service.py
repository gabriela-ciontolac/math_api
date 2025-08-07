import math
from app.cache.async_redis_cache import get_cached_result, set_cached_result

def compute_power(base: float, exp: float) -> float:
    return math.pow(base, exp)

async def compute_power_with_cache(base: float, exp: float):
    key = f"power:{base}:{exp}"
    cached = await get_cached_result(key)
    if cached is not None:
        return cached
    result = compute_power(base, exp)
    await set_cached_result(key, result)
    return result    