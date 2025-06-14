class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        while a > 0 or b > 0 or c > 0:
            x, y, z = a & 1, b & 1, c & 1
            count += (x + y if z == 0 else int(x == 0 and y == 0))
            a, b, c = a >> 1, b >> 1, c >> 1
        return count