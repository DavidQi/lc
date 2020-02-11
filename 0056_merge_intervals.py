class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []
        intervals = sorted(intervals, key=lambda x: x.start)

        result = [intervals[0]]
        for interval in intervals:
            if interval.start > result[-1].end:
                result.append(interval)
            elif result[-1].end < interval.end:
                result[-1].end = interval.end
        return result
        
