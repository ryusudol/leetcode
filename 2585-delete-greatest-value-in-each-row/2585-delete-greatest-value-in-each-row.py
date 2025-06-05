class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        # Another Approach
        for row in grid:
            row.sort(reverse=True)
        total = 0
        for i in range(len(grid[0])):
            max_val = 0
            for row in grid:
                max_val = max(max_val, row[i])
            total += max_val
        return total

        # First Approach
        # n = len(grid[0])
        # max_deleted_el_sum = 0
        # for i in range(n):
        #     max_deleted_el = 0
        #     for j in range(len(grid)):
        #         deleted_el = max(grid[j])
        #         max_deleted_el = max(max_deleted_el, deleted_el)
        #         grid[j].remove(max(grid[j]))
        #     max_deleted_el_sum += max_deleted_el
        # return max_deleted_el_sum