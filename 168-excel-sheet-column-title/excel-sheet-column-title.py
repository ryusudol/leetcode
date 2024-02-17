class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ''
        while columnNumber:
            columnNumber, remainder = divmod(columnNumber - 1, 26)
            ans = chr(65 + remainder) + ans
        return ans
            
        # ans = chr(columnNumber % 26 + 64)
        # columnNumber -= columnNumber % 26
        # while columnNumber >= 26:
        #     columnNumber = columnNumber // 26
        #     ans = chr(columnNumber + 64) + ans
        # return ans