# Написать функцию flatten, которая принимает список и возвращает указанный в примере результат. 

from timeThis import timeThis


data = [1, [2, 3], 4, 4, [5, [6], 7], 8]
result = [1, 2, 3, 4, 4, 5, 6, 7, 8]


def flatten(d: list) -> list:
    l = list()
    for i in d:
        if isinstance(i, int):
            l.append(i)
        elif isinstance(i, list):
                l += flatten(i)
    return l


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


def gen_flatten2(d: list):
    for i in d:
        if isinstance(i, list):
            yield from gen_flatten2(i)
        else:
            yield i


def gen2(d):
    return list(gen_flatten2(d))


assert timeThis(flatten)(data) == result
assert timeThis(gen_flatten)(data) == result
# assert timeThis(gen2)(data) == result
assert list(timeThis(gen_flatten2)(data)) == result
