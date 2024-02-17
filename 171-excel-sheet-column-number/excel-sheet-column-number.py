class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        columnTitle = list(columnTitle)
        columnTitle = columnTitle[::-1]
        for idx, c in enumerate(columnTitle):
            ans += (ord(c) - 64) * 26 ** idx
        return ans
