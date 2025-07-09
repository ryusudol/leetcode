class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        memo = defaultdict(list)
        longest_len, left, right = 0, 0, 0
        while right < len(s):
            is_longest_len_changed = False
            if len(memo[s[right]]) > 0:
                longest_len = max(longest_len, right - left)
                prev_left = left
                left = memo[s[right]].pop() + 1
                is_longest_len_changed = True
                for i in range(prev_left, left):
                    if len(memo[s[i]]) > 0:
                        memo[s[i]].remove(i)
            memo[s[right]].append(right)
            right += 1
            if not is_longest_len_changed:
                longest_len = max(longest_len, right - left)
        return longest_len