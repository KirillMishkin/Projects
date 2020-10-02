import time


def collatz_func(k):
    num_lst = [k]
    while k != 1:
        if k % 2 == 0:
            k //= 2
            num_lst += [k]
        else:
            k = (3 * k + 1) // 2
            num_lst += [k]
    return len(num_lst)


start = time.time()

limit = 1000000
long_chain = 0
i_max = 0

for i in range(limit // 2 - 1, limit + 1, 2):
    x = collatz_func(i)
    if x > long_chain:
        long_chain = x
        i_max = i

print(i_max)
print(time.time() - start)
