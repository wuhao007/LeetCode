class Solution:
    # @return a string
    def minWindow(self, S, T):
        exist = {}
        for t in T:
            if t in exist:
                exist[t] += 1
            else:
                exist[t] = 1
        i = -1
        j = 0
        minstr = ""
        minlen = len(S)
        while j < len(S):
            if S[j] in exist:
                if i < 0:
                    i = j
                exist[S[j]] -= 1
                if max(exist.values()) == 0:
                    while i <= j: 
                        if S[i] in exist:
                            if exist[S[i]] < 0:
                                exist[S[i]] += 1
                            else:
                                break
                        i += 1
                    if minlen >= j-i+1:
                        minstr = S[i:j+1]
                        minlen = j-i+1
                    exist[S[i]] += 1
                    i += 1

            #print S[i:j+1], i, j, exist, minstr
            j += 1
        return minstr
solution = Solution()
print solution.minWindow("ADOBECODEBANC", "ABC") == "BANC"
print solution.minWindow("acbbaca", "aba") == "baca"
print solution.minWindow("a", "a") == "a"
print solution.minWindow("a", "aa") == ""
print solution.minWindow("caae", "cae") == "caae"
print solution.minWindow("baBBba", "aB") == "aB"
print solution.minWindow("cabefgecdaecf", "cae") == "aec"
