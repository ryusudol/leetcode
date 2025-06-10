import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        total_cost = 0
        l_pq, r_pq = costs[:candidates], costs[max(len(costs) - candidates, candidates):]
        heapq.heapify(l_pq)
        heapq.heapify(r_pq)
        l_ptr, r_ptr = candidates, len(costs) - candidates - 1
        for _ in range(k):
            if not r_pq or (l_pq and l_pq[0] <= r_pq[0]):
                total_cost += heapq.heappop(l_pq)
                if l_ptr <= r_ptr:
                    heapq.heappush(l_pq, costs[l_ptr])
                    l_ptr += 1
            else:
                total_cost += heapq.heappop(r_pq)
                if l_ptr <= r_ptr:
                    heapq.heappush(r_pq, costs[r_ptr])
                    r_ptr -= 1
        return total_cost