class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dic = [0] * 256
        start, l, count = 0, 1, 0
        for i in range(len(s)):
            dic[ord(s[i])] += 1
            if dic[ord(s[i])] == 1:
                count += 1
                while count > 2:
                    dic[ord(s[start])] -= 1
                    if dic[ord(s[start]) == 0:
                        count -= 1
                    start += 1
            l = max(l, i - start + 1)
        return l
