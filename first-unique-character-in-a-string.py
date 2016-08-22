import collections
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return -1
        hs = collections.OrderedDict()
        for i in xrange(len(s)):
            c = s[i]
            if c in hs:
                del hs[c]
                hs[c] = -1
            else:
                hs[c] = i
        print hs
        return hs.popitem(last=False)[1]
solution = Solution()
print solution.firstUniqChar("loveleetcode")
print solution.firstUniqChar("dddccdbba")
