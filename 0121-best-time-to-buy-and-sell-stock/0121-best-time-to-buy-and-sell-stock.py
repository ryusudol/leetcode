class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest_price = prices[0]
        max_profit = 0
        for price in prices:
            smallest_price = min(price, smallest_price)
            max_profit = max(max_profit, price - smallest_price)
        return max_profit