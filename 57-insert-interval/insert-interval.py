class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        overlap = []
        c = 0
        start,end = 0,0
        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0] or intervals[i][0] > newInterval[1]:
                ans.append(intervals[i])
            else:
                overlap.append(intervals[i])
        overlap.append(newInterval)
        start = min(interval[0] for interval in overlap)
        end = max(interval[1] for interval in overlap)
        ans.append([start,end])
        ans.sort()
                    
        return ans
            