class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c:
            return mat
        nums = []
        for i in range(m):
            for j in range(n):
                nums.append(mat[i][j])
        ans = []
        for i in range(r):
            arr = []
            for j in range(c):
                arr.append(nums[i * c + j])
            ans.append(arr)
        return ans