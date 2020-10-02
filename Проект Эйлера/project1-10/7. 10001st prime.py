import time
from math import sqrt

def number_prime(i):
    num_prime = 0
    while True:
        i += 1
        for j in range(2, int(sqrt(i)) + 1):
            if i % j == 0:
                break
        else:
            num_prime += 1
            if num_prime >= 10001:
                return print(i)


start = time.time()
number_prime(1)
print(time.time() - start)
