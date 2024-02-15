class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]] 
        for i in range(1, numRows):
            arr = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    arr.append(1)
                else:
                    total = ans[i-1][j-1] + ans[i-1][j]
                    arr.append(total)
            ans.append(arr)
        return ans