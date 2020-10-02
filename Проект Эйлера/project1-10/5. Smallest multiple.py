
import time


def isPrime(n):
    """Поиск простых делителей числа n
    возвращает True если число простое, иначе False
    """
    div = 2
    while div * div <= n and n % div != 0:
        div += 1
    return div * div > n


start = time.time()

a = 20
lst = []  # временный лист для хранения простых чисел
answer = []  # лист для хранения простых чиле
new_lst = []  # второй временный лист для хранения простых чисел
for j in range(2, a + 1):
    for i in range(2, a + 1):
        if j % i == 0:
            if isPrime(i):
                lst.append(i)
                new_lst = list(lst)
    if len(new_lst) < 2:
        answer.append(new_lst)
    lst.clear()

number = 1
for i in range(len(answer)):
    j = 0
    number *= answer[i][j]
t = float(time.time() - start)
print(number)
print(f'{t}')
