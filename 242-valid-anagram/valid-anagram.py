class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        if len_s != len_t:
            return False
        memo = {}
        for c in s:
            int_c = ord(c)
            if int_c not in memo:
                memo[int_c] = 1
            else:
                memo[int_c] += 1
        for c in t:
            int_c = ord(c)
            if int_c not in memo or memo[int_c] == 0:
                return False
            else:
                memo[int_c] -= 1
        val_set = set(memo.values())
        if 1 in val_set:
            return False
        return True