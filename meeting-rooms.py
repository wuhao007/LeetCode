# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        time_line = []
        for interval in intervals:
            time_line += [(interval[0], 1), (interval[1], 0)]
        time_line.sort()
        n = len(intervals)
        print time_line
        for i in range(1, n):
            print time_line[i], time_line[i - 1]
            if time_line[i][1] == time_line[i - 1][1]:
                return False
        return True
solution = Solution()
print solution.canAttendMeetings([[6,10],[13,14],[12,14]])
