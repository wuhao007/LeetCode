class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        ret = 0
        heights.append(0)
        index = []
        for i in range(len(heights)):
            while len(index) > 0 and heights[index[-1]] > heights[i]:
                h = heights[index.pop()]
                sidx = index[-1] if len(index) > 0 else -1
                if h * (i - sidx - 1) > ret:
                    ret = h * (i - sidx - 1) 
            index.append(i)
        return ret
                
