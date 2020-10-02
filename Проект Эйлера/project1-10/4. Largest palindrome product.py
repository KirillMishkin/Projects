
x = 100
max_palindrome = 0

for i in range(x, 1000):
    for j in range(i, 1000):
        num = str(i * j)
        if num == num[::-1]:
            num = int(num)
            if num > max_palindrome:
                max_palindrome = num
print(max_palindrome)
