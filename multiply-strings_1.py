class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m, n = len(num1), len(num2)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                p1, p2 = i + j, i + j + 1
                s = mul + pos[p2]
                pos[p1] += s / 10
                pos[p2] = s % 10
        sb = []
        for p in pos:
            if not (len(sb) == 0 and p == 0):
                sb.append(p)
        return '0' if len(sb) == 0 else ''.join(sb)
