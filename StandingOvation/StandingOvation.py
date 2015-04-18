f = open('A-large.in', 'r')
num = int(f.readline())

def how_many(smax, audience):
    extra = 0
    friend = 0
    for i in audience:
        n = int(i)
        if n > 0:
            extra += (n - 1)
        else:
            if extra > 0:
                extra -= 1
            else:
                friend += 1
    return friend

for i in range(num):
    line = f.readline().split()
    print 'Case #' + str(i+1) + ': ' + str(how_many(int(line[0]), line[1]))
f.close()
