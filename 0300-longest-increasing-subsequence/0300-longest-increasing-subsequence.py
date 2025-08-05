class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lengths = [1]
        for i in range(1, len(nums)):
            longest_among_lower_values = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    longest_among_lower_values = max(longest_among_lower_values, lengths[j])
            lengths.append(longest_among_lower_values + 1)
        return max(lengths)