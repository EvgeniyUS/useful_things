import time
from functools import wraps


def timeThis(func):
    """ Decorator that reports the function execution time. """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Function: {func.__name__}\nExecution time: {end-start} sec')
        return result
    return wrapper
