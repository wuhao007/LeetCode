class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        def up(n, s):
            if n not in s:
                return 0
            else:
                s[n] = True
                return 1 + up(n+1, s)
        def down(n, s):
            if n not in s:
                return 0
            else:
                s[n] = True
                return 1 + down(n-1, s)
        s = dict(zip(num, [False]*len(num)))
        max_len = 0
        for n in num:
            if not s[n]:
                s[n] = True
                l = 1 + up(n+1, s) + down(n-1,s)
                if l > max_len:
                    max_len = l
        return max_len
solution = Solution()
print solution.longestConsecutive([0,-1])
