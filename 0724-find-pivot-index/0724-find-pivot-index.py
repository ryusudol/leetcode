class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum1, sum2 = 0, sum(nums[1:])
        if sum1 == sum2:
            return 0
        for i in range(1, len(nums)):
            sum1 += nums[i - 1]
            sum2 -= nums[i]
            if sum1 == sum2:
                return i
        return -1