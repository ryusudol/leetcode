class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # O(n*log(n))
        # nums.sort()
        # for i in range(len(nums)):
        #     if i != nums[i]:
        #         return i
        # return len(nums)

        # O(n)
        total = sum(nums)
        return (len(nums) * (len(nums) + 1)) // 2 - total