class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        num_set = sorted(num_set)
        set_length = len(num_set)

        if set_length == 0 or set_length == 1:
            return set_length
        
        longest_length, count = 0, 0
        for idx, num in enumerate(num_set):
            if idx == 0:
                count = 1
            elif num == num_set[idx - 1] + 1:
                count += 1
                longest_length = max(longest_length, count)
            else:
                count = 1
                longest_length = max(longest_length, count)
        
        return longest_length