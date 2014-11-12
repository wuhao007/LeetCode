class Solution:
    # @return a string
    def minWindow(self, S, T):
        mp = {}
        lenS = len(S)
        lenT = len(T)
        for t in T:
            if t in mp:
                mp[t] += 1
            else:
                mp[t] = 1
        size = 0
        ret = []
        left = 0
        for right in range(lenS):
            cRight = S[right]
            if cRight in mp:
                mp[cRight] -= 1
                if mp[cRight] == 0:
                    size += 1
                while left <= right:
                    c = S[left]
                    if c in mp:
                        if mp[c] >= 0:
                            break
                        else:
                            mp[c] += 1
                    left += 1
                if size == len(mp) and right - left + 1 == lenT:
                    ret += [left]
        return ret
solution = Solution()
print solution.minWindow('abbcdcbba','abbc')
