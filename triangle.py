triangle = []
with open('triangle.txt', 'r') as fin:
    for line in fin:
        triangle += [line.split()]
#print triangle
max_row = len(triangle)
max_value = -1
dict = {}
def dfs(row, col, value):
    global max_value
    found = int(triangle[row][col])
    key = str(row) + ':' + str(col)
    if row == max_row - 1:
        value += found
        if value > max_value:
            max_value = value
        return found
    else:
        if key in dict:
            add = dict[key]
            value += add 
            if value > max_value:
                max_value = value
            return add
        else: 
            a = dfs(row+1, col, value + found)
            b = dfs(row+1, col+1, value + found)
            add = max(a,b) + found
            dict[key] = add
            return add
    return
dfs(0, 0, 0)
print max_value
