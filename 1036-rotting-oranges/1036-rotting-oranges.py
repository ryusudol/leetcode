class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
        queue = deque()
        fresh_oranges, elapsed_time = 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                elif grid[i][j] == 2:
                    queue.append((0, i, j))
        while queue:
            cur_time, cur_x, cur_y = queue.popleft()
            elapsed_time = max(elapsed_time, cur_time)
            for i in range(4):
                next_x, next_y = cur_x + dx[i], cur_y + dy[i]
                if 0 <= next_x < m and 0 <= next_y < n and grid[next_x][next_y] == 1:
                    grid[next_x][next_y] = 2
                    fresh_oranges -= 1
                    queue.append((cur_time + 1, next_x, next_y))
        return elapsed_time if fresh_oranges == 0 else -1