class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        idx = 0
        while idx < len(nums):
            if idx != len(nums) - 1 and nums[idx] == nums[idx+1]:
                idx += 2
            else:
                return nums[idx]

        # once = []
        # memo = {}
        # for num in nums:
        #     if num not in memo:
        #         memo[num] = 1
        #         once.append(num)
        #     else:
        #         once.remove(num)
        #         memo[num] += 1
        # return once[0]