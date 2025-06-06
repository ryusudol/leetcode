class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_al = cur = 0
        for g in gain:
            cur += g
            max_al = max(max_al, cur)
        return max_al