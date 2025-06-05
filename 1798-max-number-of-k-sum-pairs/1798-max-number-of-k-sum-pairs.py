class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # Another approach
        nums.sort()
        i, j = 0, len(nums) - 1
        operations = 0
        while i < j:
            if nums[i] + nums[j] < k:
                i += 1
            elif nums[i] + nums[j] > k:
                j -= 1
            else:
                operations += 1
                i += 1
                j -= 1
        return operations

        # My original solution
        # if len(nums) == 1:
        #     return 0
        # counter = Counter(nums)
        # oprations = 0
        # for num in nums:
        #     if num in counter and k - num in counter:
        #         if (num != k - num and counter[num] > 0 and counter[k - num] > 0) or (num == k - num and counter[num] > 1):
        #             counter[num] -= 1
        #             counter[k - num] -= 1
        #             oprations += 1
        # return oprations