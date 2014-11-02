# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def merge(self, intervals):
        def insert(intervals, newInterval):
            if newInterval == None:
                return intervals
            if intervals == []:
                return [newInterval]
            i = 0
            while i < len(intervals):
                if intervals[i].end < newInterval.start:
                    i += 1
                elif newInterval.end < intervals[i].start:
                    intervals.insert(i, newInterval)
                    return intervals
                else:
                    newInterval.start = min(intervals[i].start, newInterval.start)
                    newInterval.end = max(intervals[i].end, newInterval.end)
                    intervals.pop(i)
            return intervals + [newInterval]
        result = []
        while intervals != []:
	    node = intervals.pop()
	    print node.start, node.end
            result = insert(result, node)
	    print result
        return result
interval1 = Interval(1,3)
interval2 = Interval(2,6)
interval3 = Interval(8,10)
interval4 = Interval(15,18)

solution = Solution()
for node in solution.merge([interval1, interval2, interval3, interval4]):
    print node.start, node.end
