import logging
import time
from functools import wraps

def log_performance(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = await func(*args, **kwargs)
        end_time = time.perf_counter()
        logging.info(f"Execution time for {func.__name__}: {end_time - start_time:.2f} seconds")
        return result
    return wrapper
