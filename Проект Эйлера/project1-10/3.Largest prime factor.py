# Каков самый большой делитель числа 600851475143, являющийся простым числом?
from math import sqrt


def isPrime(n):
    div = 2
    while div * div <= n and n % div != 0:
        div += 1
    return div * div > n


num = 600851475143
x = 0
answer = 0
for i in range(2, int(sqrt(num))):
    if num % i == 0:
        x = i
        if isPrime(i):
            answer = i

while x > 0:
    if x == 1:
        break
    if num % x == 0:
        j = num // x
        if isPrime(j):
            answer = j
    x -= 1

print(answer)
