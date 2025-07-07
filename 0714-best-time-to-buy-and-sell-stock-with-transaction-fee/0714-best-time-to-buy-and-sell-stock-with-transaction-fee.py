class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            prev_cash = cash
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, prev_cash - prices[i])
        return cash