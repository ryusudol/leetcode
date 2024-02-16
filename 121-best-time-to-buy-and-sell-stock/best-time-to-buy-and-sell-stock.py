class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        max_profit = 0
        left, right = 0, 1
        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit > 0:
                max_profit = max(max_profit, profit)
            else:
                left = right
            right += 1
        return max_profit