class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack)):
            for j in range(len(needle)):
                if haystack[i + j] == needle[j]:
                    if j == len(needle) - 1
                        return i
                    if i + j == len(haystack) - 1:
                        return -1
                else:
                    break 
