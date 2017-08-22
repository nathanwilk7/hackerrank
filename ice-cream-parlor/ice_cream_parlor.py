import os
import sys

def get_indices(m, n, c):
    for j in range(len(c) - 1):
        for k in range(j + 1, len(c)):
            if c[j] + c[k] == m:
                return j, k

t = int(sys.stdin.readline())
for i in range(t):
    m = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    c = [ int(x) for x in sys.stdin.readline().split(' ')]

    f, s = get_indices(m, n, c)
    print(f + 1, s + 1)
