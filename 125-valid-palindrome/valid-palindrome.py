class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        new_s = ''
        s = s.lower()
        for c in s:
            if 'a' <= c <= 'z' or '0' <= c <= '9':
                new_s += c
        left, right = 0, len(new_s) - 1
        while left <= right:
            if new_s[left] != new_s[right]:
                return False
            left += 1
            right -= 1
        return True