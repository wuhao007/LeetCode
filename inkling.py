def solution1(S):
    stack = []
    for s in S:
        if s is '+':
            try:
                stack += [stack.pop() + stack.pop()]
            except:
                return -1
        elif s is '*':
            try:
                stack += [stack.pop() * stack.pop()]
            except:
                return -1
        elif s is '0' or s is '1' or s is '2' or s is '3' or s is '4' or s is '5' or s is '6' or s is '7' or s is '8' or s is '9':
            stack += [int(s)]
        else:
            return -1
    return stack[0]
print solution1('13+62*7+*')

def solution2(K, A):
    s = {}
    count = 0
    for a in A:
        if a in s:
            s[a] += 1
        else:
            s[a] = 1
    for a in A:
        if (K - a) in s:
            count += s[K - a]
    return count
print solution2(6, [1,8,-3,0,1,3,-2,4,5])
