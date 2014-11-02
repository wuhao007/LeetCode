from sys import stdin
from sys import stdout
import math

Q = stdin.readline()
Q = float(Q)
M = stdin.readline()
M = int(M)
array = []
for i in range(M):
    line = stdin.readline()
    v, c = line.split()
    v = int(v)
    c = int(c)
    for j in range(c):
        array += [v]
N = len(array)
array.sort()
k = 1
lk = int(math.ceil(N * k / Q))
num = 0
while lk < N:
    num += 1
    stdout.write(str(array[lk - 1]) + '\n')
    k += 1
    lk = int(math.ceil(N * k / Q))


