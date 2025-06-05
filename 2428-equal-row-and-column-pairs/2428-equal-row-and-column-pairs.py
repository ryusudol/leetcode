class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Another Approach
        row_tuples = map(tuple, grid)
        col_tuples = map(tuple, zip(*grid))
        counter = Counter(row_tuples)
        total = 0
        for col in col_tuples:
            if col in counter:
                total += counter[col]
        return total

        # Brute Foce Approach
        # n, count = len(grid), 0
        # memo = {}
        # for i in range(n):
        #     for j in range(n):
        #         if grid[i][0] == grid[0][j]:
        #             is_same = True
        #             for k in range(1, n):
        #                 if grid[i][k] != grid[k][j]:
        #                     is_same = False
        #                     break
        #             if is_same:
        #                 count += 1
        # return count