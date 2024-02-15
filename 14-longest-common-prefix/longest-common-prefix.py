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
            # return ''.join([c1 for c1, c2 in zip(str1, str2) if c1 == c2])
        longest_prefix = strs[0]
        for s in strs[1:]:
            longest_prefix = common_prefix(longest_prefix, s)
        return longest_prefix

        # longest_prefix = strs[0]
        # for _str in strs[1:]:
        #     if _str == '':
        #         return ''
        #     _str = list(_str)
        #     for idx, c in enumerate(_str):
        #         if idx >= len(longest_prefix):
        #             break
        #         if c != longest_prefix[idx]:
        #             longest_prefix = longest_prefix[:idx]
        #         if idx == len(_str) - 1 and idx < len(longest_prefix) - 1:
        #             longest_prefix = longest_prefix[:idx+1]
        # return longest_prefix