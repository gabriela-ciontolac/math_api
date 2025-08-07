import math
from app.cache.async_redis_cache import get_cached_result, set_cached_result

def compute_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    elif n == 0:
        return 0
    elif n == 1: 
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    

async def compute_fibonacci_with_cache(n: int):
    key = f"fibonacci:{n}"
    cached = await get_cached_result(key)
    if cached is not None:
        return cached
    result = compute_fibonacci(n)
    await set_cached_result(key, result)
    return result
