class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest_prod = cur_max = cur_min = nums[0]
        for i in range(1, len(nums)):
            cur_val = nums[i]
            temp_max = max(cur_val, cur_val * cur_min, cur_val * cur_max)
            cur_min = min(cur_val, cur_val * cur_min, cur_val * cur_max)
            cur_max = temp_max
            largest_prod = max(cur_max, largest_prod)
        return largest_prod