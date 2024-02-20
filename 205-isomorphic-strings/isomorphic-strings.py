class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        memo1, memo2 = {}, {}
        count = 0
        comp_arr1, comp_arr2 = [0] * len(s), [0] * len(s)
        for idx, c in enumerate(s):
            if c not in memo1:
                count += 1
                memo1[c] = count
                comp_arr1[idx] = count
            else:
                comp_arr1[idx] = memo1[c]
        count = 0
        for idx, c in enumerate(t):
            if c not in memo2:
                count += 1
                memo2[c] = count
                comp_arr2[idx] = count
            else:
                comp_arr2[idx] = memo2[c]
        return comp_arr1 == comp_arr2