class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if 'A' <= word[0] <= 'Z':
            all_cap = True if 'A' <= word[-1] <= 'Z' else False
            for c in word[1:]:
                if all_cap and 'a' <= c <= 'z' or not all_cap and 'A' <= c <= 'Z':
                    return False
            return True
        else:
            for c in word:
                if 'A' <= c <= 'Z':
                    return False
            return True