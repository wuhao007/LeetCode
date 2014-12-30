def powerset(n):
    def helper(path, index):
        print path
        for i in range(index, n + 1):
            path += [i]
            helper(path, i + 1)
            path.pop()
    helper([], 1)
print powerset(2)
