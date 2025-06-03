class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # More efficient solution
        if str1 + str2 != str2 + str1:
            return ''
        _gcd = gcd(len(str1), len(str2))
        return str1[:_gcd]

        ### My solution ###
        # i = j = 0
        # x, temp = '', ''
        # while i < len(str1) and j < len(str2) and str1[i] == str2[j]:
        #     temp += str1[i]
        #     i += 1
        #     j += 1
        #     if len(str1) % len(temp) == 0 and len(str2) % len(temp) == 0:
        #         x = temp
        # if len(x) == 0 or len(str1) % len(x) != 0 or len(str2) % len(x) != 0:
        #     return x
        # for i in range(len(str1) // len(x)):
        #     if str1[len(x) * i:len(x) * (i + 1)] != x:
        #         return ''
        # for i in range(len(str2) // len(x)):
        #     if str2[len(x) * i:len(x) * (i + 1)] != x:
        #         return ''
        # return x