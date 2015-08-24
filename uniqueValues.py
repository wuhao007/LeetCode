def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    # Your code here
    d = {}
    for value in aDict.values():
        d[value] = d.get(value, 0) + 1
    print d
    return [key for key, value in aDict.items() if d[value] == 1]
print uniqueValues({1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0})
        
