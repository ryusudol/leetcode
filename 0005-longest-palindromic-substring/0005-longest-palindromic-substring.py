class Solution:
    def longestPalindrome(self, s: str) -> str:
        ##### My first approach #####
        # longest_palindrome = ''
        # max_len = 0
        # for left in range(len(s) - 1):
        #     right = len(s) - 1
        #     while left < right and right - left + 1 > max_len:
        #         while s[right] != s[left]:
        #             right -= 1
        #         is_palindrome = True
        #         l, r = left, right
        #         while l <= r:
        #             if s[l] != s[r]:
        #                 is_palindrome = False
        #                 break
        #             l += 1
        #             r -= 1
        #         if is_palindrome and max_len < right - left + 1:
        #             longest_palindrome = s[left:right + 1]
        #             max_len = max(max_len, right - left + 1)
        #             break
        #         right -= 1
        # return longest_palindrome if max_len != 0 else s[0]

        ##### Second approach #####
        max_len = 0
        longest_palindrome = s[0]
        for i in range(len(s)):
            for j in range(len(s) - 1, i, -1):
                text = s[i:j + 1]
                if text == text[::-1] and max_len < len(text):
                    longest_palindrome = text
                    max_len = len(text)
        return longest_palindrome