# Написать функцию flatten, которая принимает список и возвращает указанный в примере результат. 

data = [1, [2, 3], 4, 4, [5, [6], 7], 8]
# Результат:     1, 2, 3, 4, 4, 5, 6, 7, 8,

from timeit import timeit
import time
from functools import wraps


def timeThis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('Function: {}\nExecution time: {} sec'.format(
            func.__name__, end-start))
        return result
    return wrapper


def flatten(d: list) -> list:
    l = list()
    for i in d:
        if isinstance(i, int):
            l.append(i)
        elif isinstance(i, list):
                l += flatten(i)
    return l


@timeThis
def test(d):
    print(flatten(d))

test(data)


def gen_flatten(d: list) -> list:
    g = (i for i in d)
    l = list()
    try:
        while True:
            v = next(g)
            if isinstance(v, int):
                l.append(v)
            elif isinstance(v, list):
                    l += gen_flatten(v)
    except StopIteration:
        pass
    return l

@timeThis
def test2(d):
    print(gen_flatten(d))

test2(data)


def gen_flatten2(d: list):
    for i in d:
        if isinstance(i, list):
            yield from gen_flatten2(i)
        else:
            yield i


@timeThis
def test2(d):
    print(list(gen_flatten2(d)))

test2(data)

