import functools
from collections.abc import Callable
import time


def timeit(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"The function execution took {end_time - start_time:.2f} seconds")
        return result
    return wrapper

@timeit
def ingest():
    """
    Ingest Function
    :return:
    """
    time.sleep(2)
    pass

if __name__=='__main__':
    print(ingest.__name__)
    print(ingest.__doc__)
    print(ingest.__annotations__)
