import re
def calculateas(e):
    def calculatemd(e):
        nums = re.split(r'[*/]', e)
        ops = re.findall(r'[*/]', e)
        r = int(nums[0])
        for i in range(1, len(nums)):
            op = ops[i - 1]
            if op == '*':
                r *= int(nums[i])
            elif op == '/':
                r /= int(nums[i])
        return r
    nums = map(lambda x: calculatemd(x), re.split(r'[+-]', e))
    ops = re.findall(r'[+-]', e)
    r = int(nums[0])
    for i in range(1, len(nums)):
        op = ops[i - 1]
        if op == '+':
            r += int(nums[i])
        elif op == '-':
            r -= int(nums[i])
    return r
        
def exp(s, ops):
    e = []
    n = len(ops)
    for i in range(n):
        e += [s[i], ops[i]]
    e += [s[-1]]
    return ''.join(e) 
def dfs(ops, s, i, target):
    if i >= len(s) - 1:
        ss = exp(s, ops) 
        if target == calculateas(ss):
            print ss
            return True
        return False
    for op in ['', '+', '-', '*', '/']:
        ops += [op]
        if dfs(ops, s, i + 1, target):
            return True
        ops.pop()
    return False

def addoperator(s, target):
    n = len(s)
    ops = []
    return dfs(ops, s, 0, target)
        
print addoperator('1234', 6)
