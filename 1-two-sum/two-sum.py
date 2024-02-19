class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for idx, num in enumerate(nums):
            if target - num in store:
                return [store[target - num], idx]
            store[num] = idx

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # arr = []
        # for idx, num in enumerate(nums):
        #     arr.append((num, idx))
        # arr.sort()
        # head, tail = 0, len(arr) - 1
        # while arr[head][0] + arr[tail][0] != target:
        #     if arr[head][0] + arr[tail][0] < target:
        #         head += 1
        #     elif arr[head][0] + arr[tail][0] > target:
        #         tail -= 1
        # return [arr[head][1], arr[tail][1]]