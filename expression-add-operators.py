class Solution(object):
    def helper(self, rst, path, num, target, pos, eval, multed):
        if pos == len(num) and target == eval:
            rst += [path]
        else:
            for i in range(pos, len(num)):
                if i != pos and num[pos] == '0':
                    break
                cur = num[pos:i+1]
                val = int(cur)
                if pos == 0:
                    self.helper(rst, path + cur, num, target, i + 1, val, val)
                else:   
                    self.helper(rst, path + "+" + cur, num, target, i + 1, eval + val, val)
                    self.helper(rst, path + "-" + cur, num, target, i + 1, eval - val, -val)
                    self.helper(rst, path + "*" + cur, num, target, i + 1, eval - multed + multed * val, multed * val)
                    
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if len(num) == 0:
            return []
        rst = []
        self.helper(rst, "", num, target, 0, 0, 0)
        return rst

solution = Solution()
print solution.addOperators("123", 6)
