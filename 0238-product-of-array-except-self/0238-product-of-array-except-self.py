class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product, zero_count = prod(nums), Counter(nums)[0]
        if zero_count > 1:
            return [0 for _ in range(len(nums))]
        elif zero_count == 0:
            return [product // num for num in nums]
        else:
            product = prod([num for num in nums if num != 0])
            return [0 if num != 0 else product for num in nums]