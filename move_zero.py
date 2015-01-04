def move_zero(array):
    l = 0
    r = len(array) - 1
    while l < r:
        if array[l] != 0:
            l += 1
        elif array[r] == 0:
            r -= 1
        else:
            array[l], array[r] = array[r], array[l]
            l += 1
            r -= 1
    return array
print move_zero([1,0,2,0,0,3,4])
