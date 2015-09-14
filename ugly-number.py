class Solution(object):
    def devide(self, o, d):
        while o % d == 0:
            o /= d
        return o
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        ds = [2, 3, 5]
        for d in ds:
            num = self.devide(num, d)
        return num == 1

            
            
