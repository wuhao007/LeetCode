def fib(n):
    first = 1
    second = 1
    for _ in range(n):
        first, second = second, first + second 
        print second

print fib(5)

