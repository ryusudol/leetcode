class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        count, max_count = 0, 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
        max_count = count
        for i in range(1, len(s) - k + 1):
            if s[i - 1] in vowels:
                count -= 1
            if s[i + k - 1] in vowels:
                count += 1
            max_count = max(count, max_count)
        return max_count