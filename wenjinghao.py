words = ["book", "apple", "happy", "birthday"]

def covert(word):
    char_array = [False] * 26
    for c in word:
        index = ord(c) - ord('a')
        if not char_array[index]:
            char_array[index] = True
    num = 0
    for i in range(26):
        if char_array[i]:
            num += (1 << i)
    return num

ht = {}        
for word in words:
    num = covert(word)
    mx = ht.get(num, '')
    if len(word) > len(mx):
        ht[num] = word

array = [(key, value) for key, value in ht.items()]
n = len(array)
mx = 0
worda = ''
wordb = ''
for i in range(n):
    for j in range(i, n):
        if array[i][0] & array[j][0] == 0:
            mu = len(array[i][1]) * len(array[j][1])
            if mu > mx:
                mx = mu
                worda = array[i][1]
                wordb = array[j][1]
print worda
print wordb
                
                

