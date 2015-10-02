import heapq
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        def add(h, heap, res, x):
            if res:
                if res[-1][1] != h:
                    if res[-1][0] == x:
                        res[-1][1] = max(h, res[-1][1])
                    else:
                        res += [[x, h]]
            else:
                res += [[x, h]]
            
        road = []
        heap = []
        n = len(buildings)
        for i in range(n):
            Li, Ri, Hi = buildings[i]
            road += [[Li, 0, Hi, i], [Ri, 1, Hi, i]]
        road.sort()
        passed = set()
        res = []
        for x, t, h, i in road:
            print x, t, h, i
            if t == 0:
                heapq.heappush(heap, (-h, x, t, i))    
            else:
                passed.add(i)
                while len(heap) > 0 and heap[0][3] in passed:
                    heapq.heappop(heap)    
            if heap:
                add(-heap[0][0], heap, res, x)
            else:
                add(0, heap, res, x)
        return res

solution = Solution()
print solution.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]])
print solution.getSkyline([[0,2,3],[2,5,3]])
print solution.getSkyline([[1,2,1],[1,2,2],[1,2,3]])
