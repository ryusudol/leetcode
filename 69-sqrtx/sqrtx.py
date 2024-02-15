class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        for i in range(1, x):
            if i ** 2 == x:
                return i
            elif i ** 2 > x:
                return i - 1
            elif i == x - 1:
                return i