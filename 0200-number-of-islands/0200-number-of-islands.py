class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        def bfs(x, y):
            visited[x][y] = True
            queue = deque([(x, y)])
            while queue:
                cur_x, cur_y = queue.popleft()
                for i in range(4):
                    next_x, next_y = cur_x + dx[i], cur_y + dy[i]
                    if 0 <= next_x < n and 0 <= next_y < m and grid[next_x][next_y] == '1' and not visited[next_x][next_y]:
                        queue.append((next_x, next_y))
                        visited[next_x][next_y] = True
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and not visited[i][j]:
                    bfs(i, j)
                    num_islands += 1
        
        return num_islands