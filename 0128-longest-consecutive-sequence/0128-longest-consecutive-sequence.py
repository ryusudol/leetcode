class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sorted_nums = sorted(set(nums))
        longest_length, count = 1, 1
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i - 1] + 1 == sorted_nums[i]:
                count += 1
            else:
                longest_length = max(longest_length, count)
                count = 1
        return max(longest_length, count)
