class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[1])
        c = 1
        limit = intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0] >= limit:
                limit = intervals[i][1]
                c += 1
        return len(intervals) - c
