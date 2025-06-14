class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        while a > 0 or b > 0 or c > 0:
            bit_a, bit_b, bit_c = a & 1, b & 1, c & 1
            if bit_c == 1 and bit_a | bit_b != 1:
                count += 1
            elif bit_c == 0:
                count += (bit_a + bit_b)
            a, b, c = a >> 1, b >> 1, c >> 1
        return count