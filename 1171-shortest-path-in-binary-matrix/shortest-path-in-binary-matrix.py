class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        visited = [[False] * n for _ in range(n)]
        shortest_path_len = -1
        dx = [1, -1, 0, 0, 1, 1, -1, -1]
        dy = [0, 0, 1, -1, 1, -1, 1, -1]

        queue = deque()
        queue.append((0, 0, 1))
        visited[0][0] = True

        while queue:
            curr_x, curr_y, path_len = queue.popleft()
            if curr_x == n - 1 and curr_y == n - 1:
                shortest_path_len = path_len
                break
            for i in range(8):
                next_x = curr_x + dx[i]
                next_y = curr_y + dy[i]
                if next_x >= 0 and next_x < n and next_y >= 0 and next_y < n:
                    if grid[next_x][next_y] == 0 and not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        queue.append((next_x, next_y, path_len + 1))
        
        return shortest_path_len