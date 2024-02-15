class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = strs[0]
        for _str in strs[1:]:
            if _str == '':
                return ''
            _str = list(_str)
            for idx, c in enumerate(_str):
                if idx >= len(longest_prefix):
                    break
                if c != longest_prefix[idx]:
                    longest_prefix = longest_prefix[:idx]
                if idx == len(_str) - 1 and idx < len(longest_prefix) - 1:
                    longest_prefix = longest_prefix[:idx+1]
        return longest_prefix