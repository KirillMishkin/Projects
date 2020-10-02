import array
import struct
from pympler import asizeof

n = 10000
y = array.array('i', list(i for i in range(1, n + 1)))
z = memoryview(y)
print(z.tolist())
