class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        def dfs(s):
            if s != []:               
                ss = s[1:]
                m = len(ss)
                for i in range(m):  
                    print s[0]              
                    dfs(ss[i:])
                    print
                
        dfs(S)
s = Solution()
s.subsets([1,2,3])
            