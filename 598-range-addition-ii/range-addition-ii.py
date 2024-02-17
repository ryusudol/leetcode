class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        # matrix = [[0] * n for _ in range(m)]
        if not ops:
            return m * n
        min_a = min_b = 999999
        for op in ops:
            a, b = op
            min_a = min(min_a, a)
            min_b = min(min_b, b)
        return min_a * min_b
        # count = 0
        # max_val = max([max(row) for row in matrix])  # Finding the max value in a 2-dimensional array
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == max_val:
        #             count += 1
        # return count