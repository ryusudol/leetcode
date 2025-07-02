class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1 / val

        def dfs(cur_v, target, visited):
            if cur_v == target:
                return 1.0
            visited.add(cur_v)
            for v, val in graph[cur_v].items():
                if v not in visited:
                    result = dfs(v, target, visited)
                    if result != -1.0:
                        return val * result
            return -1.0

        ans = []
        for q in queries:
            if q[0] in graph and q[1] in graph:
                val = dfs(q[0], q[1], set()) if q[0] != q[1] else 1
                ans.append(val)
            else:
                ans.append(-1)
        return ans