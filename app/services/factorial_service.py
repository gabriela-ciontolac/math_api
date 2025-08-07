import math
from app.cache.async_redis_cache import get_cached_result, set_cached_result
 
def compute_factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

async def compute_factorial_with_cache(n: int):
    key = f"factorial:{n}"
    cached = await get_cached_result(key)
    if cached is not None:
        return cached
    # Compute factorial (replace with your own async-safe implementation if needed)
    result = compute_factorial(n)  # Assuming this is CPU-bound and safe to run in sync
    await set_cached_result(key, result)
    return result