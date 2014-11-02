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
        print mp
        size = 0
        ret = S
        left = 0
        minLen = lenS
        for right in range(lenS):
            cRight = S[right]
            print cRight
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
                if size == len(mp) and right - left + 1 < minLen:
                    ret = S[left:right + 1]
                    minLen = right - left + 1
        return ret
solution = Solution()
print solution.minWindow('a','a')

