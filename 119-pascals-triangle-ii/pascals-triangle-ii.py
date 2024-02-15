class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal = [[1]]
        for i in range(1, rowIndex + 1):
            arr = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    arr.append(1)
                else:
                    total = pascal[i-1][j-1] + pascal[i-1][j]
                    arr.append(total)
            pascal.append(arr)
        return pascal[-1]