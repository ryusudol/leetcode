class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) == 0: return t
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        for idx, c in enumerate(t):
            if idx == len(t) - 1 or c != s[idx]: return c