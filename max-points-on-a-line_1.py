# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if points == None:
            return 0
        if len(points) <= 2:
            return len(points)
        mp = {}
        result = 0
        for i in range(len(points)):
            mp.clear()
            overlap, mx = 0, 0
            for j in range(i + 1, len(points)):
                x = points[j].x - points[i].x
                y = points[j].y - points[i].y
                if x == y == 0:
                    overlap += 1
                    continue
                gcd = generateGCD(x, y)
                if gcd:
                    x /= gcd
                    y /= gcd
                if x in mp:
                    if y in mp[x]:
                        mp[x][y] += 1
                    else:
                        mp[x][y] = 1
                else:
                    m = {}
                    mp[x] = {y:1}
                mx = max(mx, mp[x][y])
            result = max(result, mx + overlap + 1)
        return result
    def generateGCD(self, a, b):
        if b == 0:
            return a
        else:
            return self.generateGCD(b, a % b)          
