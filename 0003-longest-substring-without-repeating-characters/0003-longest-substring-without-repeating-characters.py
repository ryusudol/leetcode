class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ##### My first approach #####
        # memo = defaultdict(list)
        # max_len, left, right = 0, 0, 0
        # while right < len(s):
        #     is_longest_len_changed = False
        #     if len(memo[s[right]]) > 0:
        #         max_len = max(max_len, right - left)
        #         prev_left = left
        #         left = memo[s[right]].pop() + 1
        #         is_longest_len_changed = True
        #         for i in range(prev_left, left):
        #             if len(memo[s[i]]) > 0:
        #                 memo[s[i]].remove(i)
        #     memo[s[right]].append(right)
        #     right += 1
        #     if not is_longest_len_changed:
        #         max_len = max(max_len, right - left)
        # return max_len

        ##### Improved approach #####
        last_seen = {}
        max_len, left = 0, 0
        for right in range(len(s)):
            c = s[right]
            if c in last_seen and last_seen[c] >= left:
                left = last_seen[c] + 1
            max_len = max(max_len, right - left + 1)
            last_seen[c] = right
        return max_len