class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        if k == len(arr):
            return 0
        memo = {}
        for num in arr:
            if num not in memo:
                memo[num] = 1
            else:
                memo[num] += 1
        memo = {k: v for k, v in sorted(memo.items(), key=lambda item: item[1])}
        memo = list(memo.values())
        total_num_of_el = len(memo)
        total, deduction = 0, 0
        for num in memo:
            total += num
            deduction += 1
            if total == k:
                return len(memo) - deduction
            elif total > k:
                return len(memo) + 1 - deduction