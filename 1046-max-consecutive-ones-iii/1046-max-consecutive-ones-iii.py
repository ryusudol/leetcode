class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero_indices = [idx for idx, num in enumerate(nums) if num == 0]
        if len(zero_indices) <= k:
            return len(nums)
        count, max_count = 0, 0
        for i in range(len(zero_indices) - k + 1):
            if 0 < i < len(zero_indices) - k:
                count = zero_indices[i + k] - zero_indices[i - 1] - 1
            elif i == 0:
                count = zero_indices[i + k]
            else:
                count = len(nums) - zero_indices[i - 1] - 1
            max_count = max(count, max_count)
        return max_count