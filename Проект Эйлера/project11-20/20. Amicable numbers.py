from math import sqrt
from collections import defaultdict


def friendly_number(n):
    number = {}
    for i in range(1, n):
        if i < 100:
            for div in range(1, i):
                if i % div == 0:
                    if number.get(i) is None:
                        number[i] = 0
                    number[i] += div
        elif i >= 100:
            x = int(sqrt(i))
            for div in range(1, x):
                if i % div == 0:
                    if number.get(i) is None:
                        number[i] = 0
                    number[i] += div
            for div in range(x - 1, 0, -1):
                if i % div == 0:
                    j = i // div
                    if j == i:
                        break
                    number[i] += j
    lst = []
    for i in number.items():
        lst.append(sorted(i))
    b = defaultdict(int)
    for i in lst:
        b[tuple(i)] += 1
    s = 0
    for k, v in b.items():
        if v >= 2:
            for n in k:
                s += n
    return print(s)


n = 10000
friendly_number(n)
