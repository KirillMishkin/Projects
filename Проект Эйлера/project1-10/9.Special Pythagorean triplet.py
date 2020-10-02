# a**2 +b**2 = c**2

# a+b+c = 1000
# a*b*c=???
from math import sqrt
import time

start = time.time()
num_sum = 0
for a in range(1, 1000):
    for b in range(a, 1000):
        c = a ** 2 + b ** 2
        num_sum = a + b + int(sqrt(c))
        if c % sqrt(c) == 0:
            if num_sum == 1000:
                print(a * b * int(sqrt(c)))
                break
        else:
            num_sum = 0
    if num_sum == 1000:
        break
print(time.time() - start)
