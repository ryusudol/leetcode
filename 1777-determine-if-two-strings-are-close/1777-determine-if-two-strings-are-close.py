class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2) or set(word1) != set(word2):
            return False
        counter1, counter2 = Counter(word1), Counter(word2)
        return sorted(counter1.values()) == sorted(counter2.values())