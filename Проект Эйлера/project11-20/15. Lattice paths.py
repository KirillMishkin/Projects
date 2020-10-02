import time

start = time.time()
n = 20
matrix = [[1 for el in range(n)] for el_1 in range(n)]

i = 0
j = 0
matrix[i][j] = 2
lst_max_turn = []

for i in range(0, n):
    for j in range(0, n):
        if matrix[i][j] == 2:
            j = 1
        matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
        lst_max_turn.append(matrix[i][j])

for m in matrix:
    print(*m)

print(max(lst_max_turn))
print(time.time()-start)