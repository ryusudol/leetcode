class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_count, majority_element = 0, None
        memo = {}
        for num in nums:
            if num in memo: memo[num] += 1
            else: memo[num] = 1
            if memo[num] > majority_count:
                majority_count = memo[num]
                majority_element = num
        return majority_element