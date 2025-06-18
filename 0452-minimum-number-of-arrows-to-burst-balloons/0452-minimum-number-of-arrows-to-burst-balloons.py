class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        count = 0
        cur_start, cur_end = float('inf'), float('-inf')
        for p in points:
            if p[0] > cur_end:
                count += 1
                cur_start, cur_end = p
            else:
                cur_start = max(p[0], cur_start)
                cur_end = min(p[1], cur_end)
        return count