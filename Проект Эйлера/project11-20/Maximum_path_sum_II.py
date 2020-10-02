def path_sum_2(A):
    for i in range(len(A) - 1, 0, -1):
        for j in range(1, len(A[i])):
            if A[i][j - 1] >= A[i][j]:
                A[i - 1][j - 1] += A[i][j - 1]
            elif A[i][j - 1] <= A[i][j]:
                A[i - 1][j - 1] += A[i][j]
    return print(A[0][0])


with open('Graf2', 'r', encoding='utf8') as f:
    A = []
    for i in f:
        A.append(i.split())
for line in A:
    for index, value in enumerate(line):
        line[index] = int(value)

path_sum_2(A)
