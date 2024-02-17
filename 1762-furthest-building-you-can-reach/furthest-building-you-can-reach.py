class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        pq = []
        i = 0
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            # print('diff:',diff)
            if diff <= 0:
                continue
            bricks -= diff
            heapq.heappush(pq, -diff)
            # print(pq)
            if bricks < 0:
                bricks += -heapq.heappop(pq)
                # print(pq)
                ladders -= 1
            if ladders < 0:
                return i
        return len(heights) - 1

        # height_diff = []
        # for idx, height in enumerate(heights):
        #     if idx != len(heights) - 1:
        #         if heights[idx+1] - height > 0:
        #             height_diff.append(heights[idx+1] - height)
        #         else:
        #             height_diff.append(0)
        # count = 0
        # print(height_diff)
        # for diff in height_diff:
        #     if diff <= bricks:
        #         bricks -= diff
        #         count += 1
        #     elif ladders:
        #         ladders -= 1
        #         count += 1
        #     elif diff > bricks:
        #         break
        # return count