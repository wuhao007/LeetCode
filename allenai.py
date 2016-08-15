def say_hello():
    print 'Hello, World'

#for i in xrange(5):
#    say_hello()

# Hi I am Hao
def inter(a1, a2):
    return list(set(a1) & set(a2))

#print inter([1,2,3,4], [3,4,5,6])


def inter2(a1, a2):
    hm1 = {}
    for e in a1:
        hm1[e] = hm1.get(e, 0) + 1
    res = []    
    for e in a2:
        if e in hm1:
            res.append(e)

    return list(set(res))
print inter2([1,2,3,4,4], [3,4,4,5,6])
#time: O(len(a1) + len(a2))
#space: O(min(len(a1), len(a2)))
