def dfs(array, memory):
    n = len(array)
    if memory[n - 1] is not None:
        return memory[n - 1]
    if n == 1:
        if array[0] == 0:
            memory[n - 1] = True
            return True
        else:
            memory[n - 1] = False
            return False
    elif n == 2:
        if array[0] == 1:
            memory[n - 1] = True
            return True
        if array[1] == 0:
            memory[n - 1] = dfs(array[:n - 1])
            return memory[n - 1]
        return False
    else:
        two = False
        one = False
        if array[n - 2] == 1:
            two = dfs(array[:n - 2], memory)
        if array[n - 1] == 0:
            one = dfs(array[:n - 1], memory)
        memory[n - 1] = one or two
        return memory[n - 1]

array = [1,1,1,0]
n = len(array)
one = False
two = False
if array[n - 1] == 0:
    one = dfs(array[:n - 1], [None] * n)
if array[n - 2] == 1:
    two = dfs(array[:n - 2], [None] * n)

if one and two:
    print 'onetwo'
elif one:
    print 'one'
elif two:
    print 'two'
