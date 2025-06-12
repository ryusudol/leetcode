class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = { 1: 1, 2: 2, 3: 5 }
        for i in range(4, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD
        return dp[n]