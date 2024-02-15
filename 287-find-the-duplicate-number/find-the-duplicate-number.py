class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        history = {}
        for num in nums:
            if num in history:
                return num
            history[num] = 1