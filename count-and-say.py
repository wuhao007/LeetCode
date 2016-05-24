class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        curr = ["1"]
        for i in range (1, n):
            prev = curr[:]
            curr = []
            count = 1
            for j in range(1, len(prev)):
                if prev[j] != prev[j - 1]:
                    curr += [str(count), prev[j - 1]]
                    count = 1
                else:
                    count += 1
            curr += [str(count), prev[-1]]
        return ''.join(curr)        
