class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        s = list(s)
        num = 0
        for idx, c in enumerate(s):
            if idx < len(s) - 1 and romans[c] >= romans[s[idx+1]] or idx == len(s) - 1:
                num += romans[c]
            else:
                num -= romans[c]
        return num