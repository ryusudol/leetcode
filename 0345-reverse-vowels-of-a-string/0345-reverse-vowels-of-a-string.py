class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aieouAIEOU'
        s_list = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            if s_list[i] not in vowels:
                i += 1
            elif s_list[j] not in vowels:
                j -= 1
            else:
                temp = s_list[i]
                s_list[i] = s_list[j]
                s_list[j] = temp
                i += 1
                j -= 1
        return ''.join(s_list)