import logging
import time
from functools import wraps

logger = logging.getLogger(__name__)


class Benchmark:
    @classmethod
    def performance(cls, level=logging.INFO):
        def decorator(func):
            @wraps(func)
            async def wrapper(*args, **kwargs):
                start_time = time.perf_counter()
                result = await func(*args, **kwargs)
                end_time = time.perf_counter()
                msg = f"[BENCH] {func.__name__} executed in {end_time - start_time:.2f}s"
                logger.log(level, msg)
                return result
            return wrapper
        return decorator

    @classmethod
    def sync(cls, level=logging.INFO):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                start_time = time.perf_counter()
                result = func(*args, **kwargs)
                end_time = time.perf_counter()
                msg = f"[BENCH] {func.__name__} executed in {end_time - start_time:.2f}s"
                logger.log(level, msg)
                return result
            return wrapper
        return decorator
