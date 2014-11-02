class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        exist = {}
        length = 0
        ws = len(L[0])
        for l in L:
            if l in exist:
                exist[l] += 1
                length += ws
            else:
                exist[l] = 1
                length += ws
        i = 0
        j = 0
        result = []
        def _findSubstring(S, L, ws, length):
            for i in range(0, length, ws):
                s = S[i:i+ws]
                if s in L:
                    L[s] -= 1
                    if L[s] < 0:
                        return False
                else:
                    return False
            return max(L.values()) == 0
        for i in range(len(S) - length + 1):
            if _findSubstring(S[i:i+length], exist.copy(), ws, length):
                result += [i]
            i += 1
        return result

                
solution = Solution()
print solution.findSubstring("barfoothefoobarman", ["foo", "bar"])
print solution.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"])
print solution.findSubstring("aaa", ["a", "a"])
print solution.findSubstring("abababab", ["a","b","a"])
print solution.findSubstring("aaabbbc", ["a","a","b","b","c"])
print solution.findSubstring("abaababbaba", ["ab","ba","ab","ba"])
print solution.findSubstring("a", ["a"]) == [1]
