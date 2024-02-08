from collections import Counter
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        len_of_points = len(points)
        if len_of_points == 1:
            return 1
        accs = {}
        for i in range(len_of_points - 1):
            for j in range(i + 1, len_of_points):
                x1, y1 = points[i][0], points[i][1]
                x2, y2 = points[j][0], points[j][1]
                if x1 == x2:
                    same_line = 10000 + x1
                    val = x1
                    if (same_line, val) not in accs:
                        accs[(same_line, val)] = {(x1, y1), (x2, y2)}
                    else:
                        if (x1, y1) not in accs[(same_line, val)]:
                            accs[(same_line, val)].add((x1, y1))
                        if (x2, y2) not in accs[(same_line, val)]:
                            accs[(same_line, val)].add((x2, y2))
                    continue
                acc = (y1 - y2) / (x1 - x2)
                val = y1 - acc * x1
                if (acc, val) not in accs:
                    accs[(acc, val)] = {(x1, y1), (x2, y2)}
                else:
                    if (x1, y1) not in accs[(acc, val)]:
                        accs[(acc, val)].add((x1, y1))
                    if (x2, y2) not in accs[(acc, val)]:
                        accs[(acc, val)].add((x2, y2))
        max_count_values = max(accs, key=lambda k: len(accs[k]))
        max_count = len(accs[max_count_values])
        return max_count