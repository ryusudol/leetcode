class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        memo = {}
        start = max_alp_count = 0
        for end in range(len(s)):
            memo[s[end]] = memo.get(s[end], 0) + 1
            max_alp_count = max(max_alp_count, memo[s[end]])
            if end - start + 1 - max_alp_count > k:
                memo[s[start]] -= 1
                start += 1
        return len(s) - start