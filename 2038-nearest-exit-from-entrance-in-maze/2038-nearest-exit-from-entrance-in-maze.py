class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        visited = { (entrance[0], entrance[1]): True }
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
        queue = deque()
        queue.append((0, entrance[0], entrance[1]))
        while queue:
            cur_step, cur_x, cur_y = queue.popleft()
            if cur_step != 0 and (cur_x == 0 or cur_x == m - 1 or cur_y == 0 or cur_y == n - 1):
                return cur_step
            for i in range(4):
                next_x, next_y = cur_x + dx[i], cur_y + dy[i]
                if 0 <= next_x < m and 0 <= next_y < n and maze[next_x][next_y] == '.' and (next_x, next_y) not in visited:
                    queue.append((cur_step + 1, next_x, next_y))
                    visited[(next_x, next_y)] = True
        return -1