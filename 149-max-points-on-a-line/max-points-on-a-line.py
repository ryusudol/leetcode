from collections import Counter
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        len_of_points = len(points)
        if len_of_points == 0 or len_of_points == 1:
            return len_of_points
        accs = {}
        for i in range(len_of_points - 1):
            for j in range(i + 1, len_of_points):
                curr_x, curr_y = points[i][0], points[i][1]
                next_x, next_y = points[j][0], points[j][1]
                if curr_x == next_x:
                    same_line = 10000 + curr_x
                    val = curr_x
                    if (same_line, val) not in accs:
                        accs[(same_line, val)] = {(curr_x, curr_y), (next_x, next_y)}
                    else:
                        if (curr_x, curr_y) not in accs[(same_line, val)]:
                            accs[(same_line, val)].add((curr_x, curr_y))
                        if (next_x, next_y) not in accs[(same_line, val)]:
                            accs[(same_line, val)].add((next_x, next_y))
                    continue
                acc = (curr_y - next_y) / (curr_x - next_x)
                val = curr_y - acc * curr_x
                if (acc, val) not in accs:
                    accs[(acc, val)] = {(curr_x, curr_y), (next_x, next_y)}
                else:
                    if (curr_x, curr_y) not in accs[(acc, val)]:
                        accs[(acc, val)].add((curr_x, curr_y))
                    if (next_x, next_y) not in accs[(acc, val)]:
                        accs[(acc, val)].add((next_x, next_y))
        max_count_values = max(accs, key=lambda k: len(accs[k]))
        max_count = len(accs[max_count_values])
        return max_count