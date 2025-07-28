class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, mid, end = 0, len(nums) // 2, len(nums) - 1
        while end - start > 2:
            min_val = min(nums[start], nums[mid], nums[end])
            if min_val == nums[start]:
                return nums[start]
            elif min_val == nums[mid]:
                end = mid
            else:
                start = mid
            mid = (start + end) // 2
        return min(nums[start], nums[mid], nums[end])
        # 6 7 0 1 2 3 4 5
        # 3 4 5 6 7 0 1 2
        # 0 1 2 3 4 5 6 7