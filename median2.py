class Solution:
    def median(self, nums):
        # write your code here
        from heapq import heappush, heappop 
        minheap = []
        maxheap = []
        for m in nums:
            print m
            if len(maxheap) == 0 or m <= -maxheap[0]:
                heappush(maxheap, -m)
                if len(minheap) + 1 < len(maxheap):
                    n = heappop(maxheap)
                    heappush(minheap, -n)
            elif len(minheap) == 0 or m >= minheap[0]:
                heappush(minheap, m)
                if len(minheap) > len(maxheap):
                    n = heappop(minheap)
                    heappush(maxheap, -n)
            else:
                heappush(maxheap, -m)
                if len(minheap) + 1 < len(maxheap):
                    n = heappop(maxheap)
                    heappush(minheap, -n)
        return -heappop(maxheap)
solution = Solution()
print solution.median([4,5,1,2,3])
