class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        last_non_zero_idx = len(nums) - 1
        while last_non_zero_idx >= 0 and nums[last_non_zero_idx] == 0:
            last_non_zero_idx -= 1
        zero_count = 0
        for i in range(len(nums)):
            if nums[i - zero_count] == 0:
                del nums[i - zero_count]
                zero_count += 1
        for _ in range(zero_count):
            nums.append(0)