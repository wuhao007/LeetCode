def add(source, N):
    ret = 0
    total = 0
    i = 0
    while i < len(source) and total < N:
        cur = source[i]
        if cur <= total + 1:
            total += cur
            i += 1
        else:
            ret += 1
            print "add ", total + 1
            total += (total + 1)
        print total
    return ret
print add([1,31], 31)
