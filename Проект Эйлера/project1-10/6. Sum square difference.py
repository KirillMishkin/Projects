n = 100
sum_sqrt = 0
sqrt_sum = 0
for i in range(1, n + 1):
    sum_sqrt += i
    sqrt_sum += (i ** 2)
answer = sum_sqrt**2 - sqrt_sum
print(answer)
