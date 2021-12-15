import random
from timeThis import timeThis


@timeThis
def func1(dict1):
    return [list(dict1.keys())[list(dict1.values()).index(x)] for x in reversed(sorted(dict1.values()))]


@timeThis
def func2(d):
    return sorted(d.keys(), key = lambda x: d[x], reverse = True)


D = {}
for i in range(10000):
    key = lambda: ''.join(random.choice('abcdefgxyz') for i in range(3))
    if key not in D.keys():
        D[key] = random.choice(range(1000000))

func1(D)
func2(D)



