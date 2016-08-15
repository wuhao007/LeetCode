class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mn = sys.maxint
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.stack:
            self.stack.append(x - self.mn)
            self.mn = min(self.mn, x)
        else:
            self.stack.append(0)
            self.mn = x

    def pop(self):
        """
        :rtype: void
        """
        if not self.stack:
            return 
        pop = self.stack.pop():
        if pop < 0:
            self.min = self.min + pop

    def top(self):
        """
        :rtype: int
        """
        top = self.stack[-1]
        if top > 0:
            return top + self.mn
        else:
            return self.mn

    def getMin(self):
        """
        :rtype: int
        """
        return self.mn
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
