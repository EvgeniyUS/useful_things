from timeThis import timeThis


@timeThis
def fib(n):
    a, b = 0, 1
    num = 0
    while num < n - 1:
        a, b = b, a + b
        num += 1
    return b


@timeThis
def fib2(n):
    assert n >= 0
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b
    return b


fib(200000)
fib2(200000)
