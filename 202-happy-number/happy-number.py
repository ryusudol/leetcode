class Solution:
    def isHappy(self, n: int) -> bool:
        memo = {}
        while True:
            total = 0
            n = str(n)
            for c in n:
                total += int(c) ** 2
            if total == 1:
                return True
            elif total not in memo:
                memo[total] = True
            else:
                return False
            n = total