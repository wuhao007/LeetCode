class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        hm = set([])
        for n in num:
            hm.add(n)
        mx = 0
        while len(hm) > 0:
            x = hm.pop()
            print x
            count = 1
            xn = x - 1
            while xn in hm:
                count += 1
                hm.remove(xn)
                xn -= 1
            xx = x + 1
            while xx in hm:
                count += 1
                hm.remove(xx)
                xx += 1
            mx = max(mx, count)
        return mx
solution = Solution()
print solution.longestConsecutive([0,-1])
        if node == None:
            return node
        if hasattr(node, 'visited'):
            return node.visited
        head = UndirectedGraphNode(node.label)
        node.visited = head
        head.neighbors = [self.cloneGraph(neighbor) for neighbor in node.neighbors]
        return head
Let us take n=2m. Then we have the recurrence
T(2m)=2T(2m-1)+2mlog2(2m)=2T(2m-1)+m2m
Calling T(2m) as f(m), we get that
f(m)=2f(m-1)+m2m=2(2f(m-2)+(m-1)2m-1)+m2m=4f(m-2)+(m-1)2m+m2m=4(2f(m-3)+(m-2)2m-2)+(m-1)2m+m2m=8f(m-3)+(m-2)2m+(m-1)2m+m2m
Proceeding on these lines, we get that
f(m)=2mf(0)+2m(1+2+3+?+m)=2mf(0)+m(m+1)22m=2mf(0)+m(m+1)2m-1
Hence, T(n)=nT(1)+n(log2(n)(1+log2(n))2)=T(nlog2n)
 find min {i in N ? f(i) = 0} 
 BinarySearch(A[0..N-1], value, low, high) {
      // invariants: value > A[i] for all i < low
                     value < A[i] for all i > high
      if (high < low)
          return not_found // value would be inserted at index "low"
      mid = (low + high) / 2
      if (A[mid] > value)
          return BinarySearch(A, value, low, mid-1)
      else if (A[mid] < value)
          return BinarySearch(A, value, mid+1, high)
      else
          return mid
  }

