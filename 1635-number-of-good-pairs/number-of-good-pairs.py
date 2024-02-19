class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_good_pairs = 0
        memo = {}
        for num in nums:
            memo[num] = memo.get(num, 0) + 1
        for i in range(len(nums)):
            if memo[nums[i]] != 0:
                num_good_pairs += memo[nums[i]] * (memo[nums[i]] - 1) // 2
                memo[nums[i]] = 0
        return num_good_pairs