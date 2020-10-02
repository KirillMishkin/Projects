from collections import deque


def path_sum(numbers):
    A = []
    for i in numbers:
        A.append(i.split())
    for i in A:
        for index, v in enumerate(i):
            i[index] = int(v)
    lst = []
    for i in range(len(A) - 1, 0, -1):
        for j in range(1, len(A[i])):
            if A[i][j - 1] >= A[i][j]:
                A[i - 1][j - 1] += A[i][j - 1]
            elif A[i][j - 1] <= A[i][j]:
                A[i - 1][j - 1] += A[i][j]
    return A[0][0]


n = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''.split('\n')
path_sum(n)

'''
python -m timeit -n 1000 -s "import Maximum_path_sum_I" "Maximum_path_sum_I.path_sum"
1000 loops, best of 5: 37.7 nsec per loop

'''