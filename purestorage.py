class Solution:
    def __init__(self):
        self.count = 0
    def f(self, x):
        self.count += 1
        if x < 1:
            return 1
        else:
            return self.f(x - 1) + self.g(x)
    def g(self, x):
        self.count += 1
        if x < 2:
            return 1
        else:
            return self.f(x - 1) + self.g(x/2)
    def print_count(self):
        print self.count
        self.count = 0

solution = Solution()
solution.f(1)
solution.print_count()
solution.f(2)
solution.print_count()
solution.f(4)
solution.print_count()
solution.f(8)
solution.print_count()
solution.f(16)
solution.print_count()

