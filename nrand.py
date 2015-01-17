import sys, random
def nrand(n):
    bucket_size = sys.maxint / n
    r = n
    while r >= n:
        r = random.randint(0, sys.maxint) / bucket_size
    return r
print nrand(6) + 1

