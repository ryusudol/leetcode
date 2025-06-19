class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        graph = {}
        for i in range(len(isConnected)):
            graph[i] = []
            for j in range(len(isConnected)):
                if i != j and isConnected[i][j] == 1:
                    graph[i].append(j)
        
        # BFS
        # def bfs(cur_v):
        #     visited[cur_v] = True
        #     queue = deque()
        #     queue.append(cur_v)
        #     while queue:
        #         new_v = queue.popleft()
        #         for v in graph[new_v]:
        #             if v not in visited:
        #                 visited[v] = True
        #                 queue.append(v)

        # DFS
        def dfs(cur_v):
            visited[cur_v] = True
            for v in graph[cur_v]:
                if v not in visited:
                    dfs(v)
        
        visited = {}
        for i in range(len(isConnected)):
            if i not in visited:
                # bfs(i)
                dfs(i)
                count += 1
        
        return count
