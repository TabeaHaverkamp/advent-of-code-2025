import time
from functools import wraps

def time_function(func):
    """
    A decorator that measures and prints the execution time of a function.
    ... (rest of the time_function code)
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # ... timing logic ...
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {elapsed_time:.4f} seconds.")
        return result
    return wrapper