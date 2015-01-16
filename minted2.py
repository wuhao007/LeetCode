- Write two functions that calculate the factorial of some integer N. One function should be recursive, and one iterative.
-- Bonus points for a third using functional constructs like map, reduce, etc.

Hint: 2! -> 2*1, 1! -> 1, 0! -> 1
- Factorial is defined on 0, but it's a special case.

(1) 
def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        return -1 # error situation
    else:
        return n * factorial(n - 1)
        
(2) 

def factorial(n):
    ret = 1
    for i in range(1, n + 1):
        ret *= i
    return ret
    
(3)
reduce(*, [i for i in range(1, n + 1)])


Write a function that takes an unordered list of integers, and some integer N. This function will return a list
of all pairs of integers in the list that sum to N.
Example: arr = [1, 5, 3, 8, 5, 2, 0], N = 8 -> [(0, 8), (5, 3)]
def twosum(arr, N):
    ht = set()
    ret = []
    for num in arr:
        left = N - num
        if left in ht:
            ret += [(left, num)]
        ht.add(num)
    return ret
O(n)

https://projecteuler.net/problem=9
// (a + b + c) * (a + b + c) = a^2 + b^2 + c^2 + 2ab + 2bc + 2ac = 2c^2 + 2ab + 2

a*a + b*b + c*c = 1000 -> c*c = 

# you have a square root function, sqrt

def puzzle():
    ret = []
    for a in range(1, 1000/ 3 + 1):
        for b in range(a, 1000 / 2 + ):
            # calculate c correctly
            c2 = 1000 - a * a - b * b
            c = None
            if c2 > 0:
                c = sqrt(c2)
            else:
                continue
            if a * a + b * b + c * c == 1000:
                ret += [(a, b, c)]
    return ret
