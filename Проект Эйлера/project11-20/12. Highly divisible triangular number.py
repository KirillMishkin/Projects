import time


def triangular_div(n):
    prime = 2  # minimum prime
    lst = []  # prime sheet
    multiplication = 1
    s = n * (n + 1) // 2
    while True:
        if s % prime == 0:
            s //= prime
            lst.append(prime)
        else:
            prime += 1
        if s == 1:
            for dig in set(lst):
                multiplication *= (lst.count(dig) + 1)
            if multiplication >= 500:
                return True
            else:
                return False


start = time.time()
i = 1
while True:
    if triangular_div(i):
        Tn = ((i+1)*i)//2
        print(Tn)
        break
    i += 1
print(time.time() - start)
