class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        if len(s) == 1:
            return -1
        memo = {}
        for idx, c in enumerate(s):
            if c not in memo:
                memo[c] = (idx, -1)
            else:
                memo[c] = (memo[c][0], idx)
        max_count = -1
        for i in range(len(s)):
            if memo[s[i]]:
                start, end = memo[s[i]]
                max_count = max(max_count, end - start - 1)
                memo[s[i]] = False
        return max_count