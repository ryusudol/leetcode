class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n > 45 or k >= n:
            return []
        ans = []
        def backtrack(start, cur_sum, path):
            if cur_sum > n or len(path) > k:
                return
            for i in range(start, 10):
                path.append(i)
                if cur_sum + i == n and len(path) == k:
                    ans.append(path.copy())
                else:
                    backtrack(i + 1, cur_sum + i, path)
                path.pop()
        backtrack(1, 0, [])
        return ans