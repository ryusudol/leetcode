class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count, prev = 0, intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev[1]:
                prev = intervals[i] if intervals[i][1] < prev[1] else prev
                count += 1
            else:
                prev = intervals[i]
        return count