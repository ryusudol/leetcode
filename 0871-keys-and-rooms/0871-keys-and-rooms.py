class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = { 0: True }
        def dfs(room: List[int]):
            for key in room:
                if key not in visited:
                    visited[key] = True
                    dfs(rooms[key])
        dfs(rooms[0])
        return len(visited.keys()) == len(rooms)