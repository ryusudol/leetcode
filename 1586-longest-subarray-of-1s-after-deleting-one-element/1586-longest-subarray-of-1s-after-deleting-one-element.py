class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        left = right = count = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                count += 1
            if count > 1:
                left += 1
                if nums[left - 1] == 0:
                    count -= 1
        return len(nums) - left - 1