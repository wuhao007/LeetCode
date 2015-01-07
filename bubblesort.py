def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(i):
            if array[j] > array[i]:
                array[i], array[j] = array[j], array[i]
    return array
array = [1,4,5,2,7,4,7,9,3,2]
print bubble_sort(array) == sorted(array)
