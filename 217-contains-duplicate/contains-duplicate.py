class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

        # memo = {}
        # for num in nums:
        #     if num not in memo:
        #         memo[num] = 1
        #     else:
        #         return True
        # return False