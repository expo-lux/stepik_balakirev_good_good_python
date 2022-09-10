import time
from functools import wraps

def execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"время выполнения: {end-start}")
        return result
    return wrapper

@execution_time
def some_func(end_char: str):
    """ help """
    print("some_func" + end_char)
    time.sleep(0.1)

some_func('!')
print(some_func.__doc__)
print(some_func.__name__)
