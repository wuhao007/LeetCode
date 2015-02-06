class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        result = []
        for i in range(len(s) - 10):
            sub = s[i : i + 10]
            if s.find(sub, i + 10) != -1:
                result += [sub]
        return result
solution = Solution()
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print solution.findRepeatedDnaSequences(s)

