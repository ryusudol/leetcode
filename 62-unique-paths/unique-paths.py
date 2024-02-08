class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        unique_paths = [[1] * n for _ in range(m)]
        curr_x, curr_y = 1, 1
        for curr_x in range(1, m):
            for curr_y in range(1, n):
                prev_x, prev_y = curr_x - 1, curr_y - 1
                unique_paths[curr_x][curr_y] = unique_paths[prev_x][curr_y] + unique_paths[curr_x][prev_y]
        return unique_paths[m-1][n-1]