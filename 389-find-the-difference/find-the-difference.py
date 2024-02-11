class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) == 0:
            return t
        memo = {}
        for c in s:
            if c not in memo: memo[c] = 1
            else: memo[c] += 1
        for c in t:
            if c not in memo: return c
            else: memo[c] -= 1
        for el in memo:
            if memo[el] == -1:
                return el