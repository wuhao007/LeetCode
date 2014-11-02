class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        min_len = len(strs[0])
        min_i = 0
        for i in range(len(strs)):
            s = strs[i]
            if min_len > len(s):
                min_len = len(s)
                min_i = i
        def longestCommonPrefix(strs, prefix):
            if strs == []:
                return prefix
            for i in range(len(prefix)):
                if strs[0][i] != prefix[i]:
                    return longestCommonPrefix(strs[1:], prefix[:i])
            return longestCommonPrefix(strs[1:], prefix)
                
        return longestCommonPrefix(strs, strs[min_i])
solution = Solution()
print solution.longestCommonPrefix(['aaasdc', 'aaab', 'aaabc'])
