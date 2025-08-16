class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = [nums[0]]
        for i in range(1, len(nums)):
            sums.append(max(nums[i] + sums[i - 1], nums[i]))
        return max(sums)