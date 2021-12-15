import random
import time
from timeThis import timeThis


numbers = [random.randint(0, 1000) for i in range(10000)]


@timeThis
def bubble_sort(values):
    n = 1
    while n < len(values):
        for i in range(len(values) - n):
            if values[i] > values[i + 1]:
                values[i], values[i + 1] = values[i + 1], values[i]
        n += 1
    return values


def quick_sort(values):
    if len(values) <= 1:
        return values
    else:
        q = random.choice(values)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in values:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quick_sort(s_nums) + e_nums + quick_sort(m_nums)


# bubble_sort(numbers)

timeThis(quick_sort)(numbers)

start = time.time()
numbers.sort()
end = time.time()
print(end-start)

# print(numbers)