class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        h = {}
        for s in strings:
            a = ord(s[0])
            k = ''.join(map(lambda x: chr((x - a) % 26), ord(c) for c in s))
            h[k] = h.get(k, []) + [s]
        return sorted(h.values())
solution = Solution()
print solution.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])

