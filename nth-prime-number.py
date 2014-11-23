import math
def calcPrime(inp):
    arr = [2]
    counter = 3;
    while len(arr) < inp:
        flag = True
        bar = math.sqrt(counter)
        for i in arr:
            if counter % i == 0:
                flag = False
                break
            if i > bar:
                break
        if flag:
            arr += [counter]
        counter += 2
    return arr
print calcPrime(1000)
