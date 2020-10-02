from math import sqrt
import time

start = time.time()

def friendly_number(i):
    s = 0
    x = int(sqrt(i))
    for div in range(1, x):
        if i % div == 0:
            s += div
    for div in range(x - 1, 0, -1):
        if i % div == 0:
            j = i // div
            if j == i:
                break
            s += j
    return s


n = 10000
answer_1 = tuple(i for i in range(1, n))
answer = 0

for i in answer_1:
    num_1 = friendly_number(i)
    if num_1 == 1 and num_1 <= i // 2:
        continue
    num_2 = friendly_number(num_1)
    if num_2 == i and num_1 != i:
        answer += num_2

print(answer)
print(time.time() - start)
