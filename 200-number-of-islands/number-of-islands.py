from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        num_of_islands = 0
        visited = [[False] * n for _ in range(m)]

        def bfs(x, y):
            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]
            queue = deque()
            queue.append((x, y))
            visited[x][y] = True
            while queue:
                curr_x, curr_y = queue.popleft()
                for i in range(4):
                    next_x = curr_x + dx[i]
                    next_y = curr_y + dy[i]
                    if next_x >= 0 and next_x < m and next_y >= 0 and next_y < n:
                        if grid[next_x][next_y] == '1' and not visited[next_x][next_y]:
                            queue.append((next_x, next_y))
                            visited[next_x][next_y] = True
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    bfs(i, j)
                    num_of_islands += 1
        
        return num_of_islands