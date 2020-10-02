from time import time
start = time()
lst = []
with open('number.txt') as inf:
    for i in inf:
        j = i.strip()
        if '-' in j:
            j = j.replace('-', '')
        if ' ' in j:
            j = j.replace(' ', '')
        lst.append(j)
s = 0
for i in lst:
    s += len(i)
print(s)
print(time()-start)