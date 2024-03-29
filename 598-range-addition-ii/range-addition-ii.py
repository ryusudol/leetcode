class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n
        min_a = min_b = 999999
        for op in ops:
            a, b = op
            min_a = min(min_a, a)
            min_b = min(min_b, b)
        return min_a * min_b