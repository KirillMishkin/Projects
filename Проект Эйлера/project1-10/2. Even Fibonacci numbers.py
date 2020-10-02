n_max = 4000000

i = 0
j = 1
answer = 0
while True:
    x = i + j
    if x % 2 == 0:
        answer += x
        if answer > n_max:
            break
    if i < j:
        x, i = i, x
    else:
        x, j = j, x
print(answer)
