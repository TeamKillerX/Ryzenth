import logging
import time
from functools import wraps

logger = logging.getLogger(__name__)

def log_performance(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        ok = await func(*args, **kwargs)
        end_time = time.perf_counter()
        logger.info(f"Execution time for {func.__name__}: {end_time - start_time:.2f} seconds")
        return ok
    return wrapper

def sync_log_test(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        ok = func(*args, **kwargs)
        end_time = time.perf_counter()
        logger.info(f"Execution time for {func.__name__}: {end_time - start_time:.2f} seconds")
        return ok
    return wrapper
