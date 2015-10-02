class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0
        num = 0
        sign = '+'
        stack = []
        for i in range(n):
            c = s[i]
            if c.isdigit():
                num = num * 10 + ord(c) - ord('0')
            if (not c.isdigit() and c != ' ') or i == n - 1:
                if sign == '+':
                    stack += [num]
                elif sign == '-':
                    stack += [-num]
                elif sign == '*':
                    stack += [stack.pop() * num]
                elif sign == '/':
                    stack += [stack.pop() / float(num)]
                sign = c
                num = 0
            print stack
        return sum(stack)
solution = Solution()
print solution.calculate("14-3/2")

