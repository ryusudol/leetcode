import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        if n == 1:
            return 0
        used_counts = [0 for _ in range(n)]
        rooms = [(0, i) for i in range(n)]
        meetings.sort()
        for start, end in meetings:
            min_room_idx = min_idx = 999
            for idx, room in enumerate(rooms):
                released_time, room_number = room
                if released_time <= start:
                    prev_idx = min_room_idx
                    min_room_idx = min(min_room_idx, room_number)
                    if min_idx == 999 or prev_idx != min_room_idx:
                        min_idx = idx
            if min_room_idx == 999:
                released_time, min_room_idx = heapq.heappop(rooms)
            else:
                released_time, _ = rooms.pop(min_idx)
            used_counts[min_room_idx] += 1
            if released_time >= start:
                heapq.heappush(rooms, (released_time + end - start, min_room_idx))
            else:
                heapq.heappush(rooms, (end, min_room_idx))
            heapq.heapify(rooms)
        max_used_count = max(used_counts)
        return used_counts.index(max_used_count)