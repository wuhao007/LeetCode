def moveZero(A):
    l = 0
    for i in range(len(A)):
        if A[i] != 0:
            A[l], A[i] = A[i], A[l]
            l += 1
    print A
    return len(A) - l
print moveZero([1,0,2,0,3,0,4,0,5,0])
print moveZero([1,0,0,2])
