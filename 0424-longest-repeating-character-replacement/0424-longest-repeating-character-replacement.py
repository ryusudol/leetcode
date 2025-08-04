class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        memo = {}
        start, end = 0, 0
        while end < len(s):
            if s[end] not in memo:
                memo[s[end]] = 1
            else:
                memo[s[end]] += 1
            cur_counts = memo.values()
            if sum(cur_counts) - max(cur_counts) > k:
                memo[s[start]] -= 1
                if memo[s[start]] == 0:
                    del memo[s[start]]
                start += 1
            end += 1
        return max(end - start, 1)