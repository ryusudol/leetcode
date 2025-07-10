class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for left in range(len(s)):
            for right in range(left, len(s)):
                text = s[left:right + 1]
                if text == text[::-1]:
                    count += 1
        return count