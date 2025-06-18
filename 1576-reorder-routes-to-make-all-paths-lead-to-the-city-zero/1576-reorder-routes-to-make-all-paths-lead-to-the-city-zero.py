class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        count = 0
        grid = [[] for _ in range(n)]
        for c in connections:
            grid[c[0]].append(c[1])
            grid[c[1]].append(-c[0])
        visited = { 0: True }
        queue = deque([0])
        while queue:
            cur = queue.popleft()
            for v in grid[cur]:
                if abs(v) not in visited:
                    if v > 0:
                        count += 1
                    visited[abs(v)] = True
                    queue.append(abs(v))
        return count