def NSum(array, N):
    f = [False] * (((N + 1) * N) / 2 + 1)
    s = 0
    i = 1
    j = 0
    cnt = 0
    while i <= N:
        print i, j
        if j < len(array) and array[j] == i:
            j += 1
            f[i] = True
            s += i
            f[s] = True
            for k in range(1, s):
                if f[k]:
                    f[s - k] = True
        elif i < array[j]:
            l = s - i
            if f[i] or f[l]:
                f[i] = True
            else:
                cnt += 1
                f[i] = True
                s += i
                print "add", i
                f[s] = True
                for k in range(1, s):
                    if f[k]:
                        f[s - k] = True
        i += 1
    return cnt
print NSum([1,3], 3)
print NSum([1,3], 7)
print NSum([1,2,3,7,9,10], 10)
