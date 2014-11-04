def serialize(words):
    return ''.join([str(len(x)) + '|' + x for x in words])
test = ['happy','new','year']
print serialize(test)

def deserialize(string):
    i = 0
    ret = []
    j = i
    num = None
    while j < len(string):
        if string[j] == '|':
            num = int(string[i:j])
            ret += [string[j + 1:j + 1 + num]]
            i = j + 1 + num
            j = i + 1
        else:
            j += 1
    return ret
print deserialize(serialize(test)) == test

            


