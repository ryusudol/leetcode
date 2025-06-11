class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums[0], nums[1]) if n == 2 else nums[0]
        memo = { 0: nums[0], 1: nums[1], 2: nums[0] + nums[2] }
        for i in range(3, n):
            memo[i] = max(memo[i - 2], memo[i - 3]) + nums[i]
        return max(memo[n - 1], memo[n - 2])