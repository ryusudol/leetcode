class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def common_prefix(str1, str2):
            res = ''
            for idx, c in enumerate(str1):
                if idx < len(str2) and c == str2[idx]:
                    res += c
                else:
                    break
            return res
        longest_prefix = strs[0]
        for s in strs[1:]:
            longest_prefix = common_prefix(longest_prefix, s)
        return longest_prefix