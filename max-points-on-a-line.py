# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if len(points) < 3:
            return len(points)
        tan_hash = {}
        point_hash = {}
        for i in range(len(points)):
            if (points[i].x, points[i].y) in point_hash:
                point_hash[(points[i].x, points[i].y)] += 1
                continue
            else:
                point_hash[(points[i].x, points[i].y)] = 1
            tan_hash[points[i]] = {}
            slope = tan_hash[points[i]]
            for j in range(len(points)):
                if points[i].x != points[j].x or points[i].y != points[j].y:
                    if points[i].x == points[j].x:
                        if 'v' in slope:
                            slope['v'] += [points[j]]
                        else:
                            slope['v'] = [points[j]]
                    else:
                        tan = (points[j].y - points[i].y) * 1.0 / (points[j].x - points[i].x)
                        if tan in slope:
                            slope[tan] += [points[j]]
                        else:
                            slope[tan] = [points[j]]
        start = points[0]
        max_num = point_hash[(start.x, start.y)]
        for start, tan_list in tan_hash.iteritems():
            for tan, point_list in tan_list.iteritems():
                print '(', start.x, start.y, ')', tan, len(point_list), point_hash[(start.x, start.y)]
                if len(point_list) + point_hash[(start.x, start.y)] > max_num:
                    max_num = len(point_list) + point_hash[(start.x, start.y)]
        return max_num
point1 = Point(1,1)
point2 = Point(1,1)
point3 = Point(1,1)
point4 = Point(1,1)
points = [point1, point2, point3, point4]
solution = Solution()
print solution.maxPoints(points)

