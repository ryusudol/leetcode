class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        once = []
        memo = {}
        for num in nums:
            if num not in memo:
                memo[num] = 1
                once.append(num)
            else:
                once.remove(num)
                memo[num] += 1
        return once[0]