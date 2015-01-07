Hi Julien, I am Hao

array = set([])
def fun(array):
    result = [[]]
    for e in array:
        new_array = reault[:]
        for lst in new_array:
            lst += [e]
        result += [s for s in new_array]
    return result 
    
    
def permutation(string):
    lst = sorted(string)
    def dfs(lst, path, ret):
        
        if len(lst) == 0:
            ret += [path[:]]
            return
            
        n = len(lst)
        for i in range(n):
            k = lst.pop(i)
            path += [k]
            dfs(lst, path, ret)
            path.pop()
            lst.insert(i, k)
    
    ret = []
    dfs(lst, [], ret)
    return ret
