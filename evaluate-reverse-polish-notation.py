class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        S = []
        for s in tokens:
            if s == '+':
                S.append(S.pop() + S.pop())
            elif s == '/':
                a = S.pop()
                b = S.pop()
                S.append(a / b)
            elif s == '*':
                S.append(S.pop() * S.pop())
            elif s == '-':
                a = S.pop()
                b = S.pop()
                S.append(a - b)
            else:
                S.append(int(s))
        return s.pop()
