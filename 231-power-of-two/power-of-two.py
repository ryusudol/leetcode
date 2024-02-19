class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1: return True
        elif n < 1 or n % 2 == 1: return False
        while n != 2:
            remainder = n % 2
            if remainder != 0:
                return False
            n = n // 2
        return True