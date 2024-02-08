class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        for idx, num in enumerate(nums):
            arr.append((num, idx))
        arr.sort()
        head, tail = 0, len(arr) - 1
        while arr[head][0] + arr[tail][0] != target:
            if arr[head][0] + arr[tail][0] < target:
                head += 1
            elif arr[head][0] + arr[tail][0] > target:
                tail -= 1
        return [arr[head][1], arr[tail][1]]