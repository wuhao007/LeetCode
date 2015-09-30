import heapq
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        road = []
        heap = []
        for i in range(len(buildings)):
            Li, Ri, Hi = buildings[i]
            road += [[Li, 1, Hi, i], [Ri, 0, Hi, i]]
        road.sort()
        passed = set()
        res = []
        for x, t, h, i in road:
            print x, t, h, i
            if t == 1:
                heapq.heappush(heap, (h, x, t, i))    
            else:
                passed.add(i)
                while len(heap) > 0 and heap[0][3] in passed:
                    heapq.heappop(heap)    
            print res[-1]
            res += [(x, heap[0][0])] if heap else [(x, 0)] 
        return res

solution = Solution()
print solution.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]])
