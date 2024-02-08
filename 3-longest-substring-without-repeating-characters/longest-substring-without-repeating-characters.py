class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        compare = {}
        longest_length = 0
        for idx, c in enumerate(s):
            int_c = ord(c)
            if int_c not in compare:
                compare[int_c] = idx
                longest_length = max(longest_length, len(compare))
            else:
                val = compare[int_c]
                keys_to_check = list(compare.keys())
                for key in keys_to_check:
                    if compare[key] < val:
                        del compare[key]
                compare.pop(int_c)
                compare[int_c] = idx
        return longest_length