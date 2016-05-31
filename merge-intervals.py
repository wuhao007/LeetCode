# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key = lambda x : x[0])
        result = []
        start, end = intervals[0].start, intervals[0].end
        for interval in intervals:
            if interval.start <= end:
                end = max(end, interval.end)
            else:
                result.append(Interval(start, end))
                start, end = interval.start, interval.end
        result.append(Interval(start, end)
        return result
                
