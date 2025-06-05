class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        max_total = total
        for i in range(1, len(nums) - k + 1):
            total = total - nums[i - 1] + nums[i + k - 1]
            max_total = max(max_total, total)
        return max_total / k