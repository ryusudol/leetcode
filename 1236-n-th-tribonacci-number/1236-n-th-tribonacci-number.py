class Solution:
    memo = { 0: 0, 1: 1, 2: 1 }

    def tribonacci(self, n: int) -> int:
        for i in range(3, n + 1):
            self.memo[i] = self.memo[i - 1] + self.memo[i - 2] + self.memo[i - 3]
        return self.memo[n]