class Solution:
    def firstUniqChar(self, s: str) -> int:
        memo = {}
        for c in s:
            memo[c] = memo.get(c, 0) + 1
        for i in range(len(s)):
            if memo[s[i]] == 1:
                return i
        return -1
        # arr = [(0, -1)] * 26  # count, first_idx
        # for idx, c in enumerate(s):
        #     arr_idx = ord(c) - 97
        #     count, first_idx = arr[arr_idx]
        #     count = count + 1
        #     if count == 1: first_idx = idx
        #     arr[arr_idx] = (count, first_idx)
        # for c in s:
        #     arr_idx = ord(c) - 97
        #     count, first_idx = arr[arr_idx]
        #     if count == 1:
        #         return first_idx
        # return -1