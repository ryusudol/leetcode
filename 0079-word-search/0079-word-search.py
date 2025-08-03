class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        visited = [[False] * n for _ in range(m)]
        
        def dfs(x, y, order):
            if order == len(word) - 1:
                return True
            visited[x][y] = True
            for i in range(4):
                next_x, next_y = x + dx[i], y + dy[i]
                if 0 <= next_x < m and 0 <= next_y < n:
                    if not visited[next_x][next_y] and board[next_x][next_y] == word[order + 1]:
                        if dfs(next_x, next_y, order + 1):
                            return True
            visited[x][y] = False
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        
        return False