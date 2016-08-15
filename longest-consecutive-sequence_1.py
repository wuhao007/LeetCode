iclass Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        mp = {}
        for n in nums:
            if n in mp:
                left, right = mp[n-1] if (n-1) in mp else 0, mp[n+1] if (n+1) in mp else 0
                sm = left + right + 1
                mp[n] = sm
                res = max(res, sm)
                mp[n - left] = sm
                mp[n + right] = sm
            else:
                continue
        return res
