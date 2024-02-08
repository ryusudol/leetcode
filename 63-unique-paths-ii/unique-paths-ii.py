class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        unique_paths = [[0] * n for _ in range(m)]
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        unique_paths[0][0] = 1
        for i in range(m):
            for j in range(n):
                prev_x, prev_y = i - 1, j - 1
                if obstacleGrid[i][j] == 1:
                    continue
                if prev_x >= 0:
                    unique_paths[i][j] += unique_paths[prev_x][j]
                if prev_y >= 0:
                    unique_paths[i][j] += unique_paths[i][prev_y]
        return unique_paths[m-1][n-1]