class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        roots = [i for i in range(n)]
        for e in edges:
            root1, root2 = self.find(roots, e[0]), self.find(roots, e[1])
            
            if root1 != root2:
                roots[root1] = root2
                n -= 1
        return n
    def find(self, roots, i):
        while roots[i] != i:
            roots[i] = roots[roots[i]] 
            i = roots[i]
        return i
            
      
