class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        ans = []
        def backtrack(idx, cur):
            if len(cur) == len(digits):
                ans.append(cur)
                return
            candidates = phone_map[digits[idx]]
            for c in candidates:
                backtrack(idx + 1, cur + c)
        backtrack(0, '')
        return ans