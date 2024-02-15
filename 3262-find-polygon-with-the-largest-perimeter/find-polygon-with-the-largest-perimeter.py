class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        total = sum(nums)
        nums.sort(reverse=True)
        for num in nums:
            total = total - num
            if num < total: return total + num
        return -1