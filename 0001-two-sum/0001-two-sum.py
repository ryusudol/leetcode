class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for idx, num in enumerate(nums):
            if target - num in memo:
                return [memo[target - num], idx]
            memo[num] = idx