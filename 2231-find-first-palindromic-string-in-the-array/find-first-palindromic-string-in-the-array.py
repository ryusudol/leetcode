class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            left, right = 0, len(word) - 1
            palindrome = True
            while left <= right:
                if word[left] != word[right]:
                    palindrome = False
                    break
                left += 1
                right -= 1
            if not palindrome: continue
            else: return word
        return ''