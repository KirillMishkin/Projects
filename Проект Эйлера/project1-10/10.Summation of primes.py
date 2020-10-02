from math import sqrt
import time
import functools


@functools.lru_cache()
def IsPrime(n):
    for j in range(2, int(sqrt(n)) + 1):
        if n % j == 0:
            break
    else:
        return True


@functools.lru_cache()
def prime_top(n):
    i = 5
    prime_sum = 5
    while i <= n:
        if IsPrime(i):
            prime_sum += i
        i += 2
        if IsPrime(i):
            prime_sum += i
        i += 4
    return prime_sum


start = time.time()
m = 2000000

print(prime_top(m))
print(time.time() - start)

# Другой вариант Более быстрый
'''
num = 10
n = [2, *range(3, num + 1, 2)]
for i in range(1, len(n)):
    if n[i]:
        for j in range(3 * i + 1, len(n), n[i]):
            n[j] = False
n = [k for k in n if k]
print(sum(n))
'''
