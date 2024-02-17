class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ''
        words = s.split()
        for idx, word in enumerate(words):
            word = word[::-1]
            ans += word
            if idx != len(words) - 1:
                ans += ' '
        return ans