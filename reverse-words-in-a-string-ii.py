class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        self.reverse(s, 0, len(s) - 1)
        start, end = 0, -1
        for i in range(len(s)):
            if s[i] == ' ':
                self.reverse(s, start, i - 1)
                start = i + 1
        self.reverse(s, start, len(s) - 1))
    def reverse(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start, end = start + 1, end - 1
