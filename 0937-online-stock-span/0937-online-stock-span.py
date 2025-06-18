class StockSpanner:
    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        # Faster Approach
        if not self.prices or self.prices[-1][0] > price:
            self.prices.append((price, 1))
            return 1
        result = 1
        while self.prices and self.prices[-1][0] <= price:
            _, span = self.prices.pop()
            result += span
        self.prices.append((price, result))
        return result

    # My First Approach
    # def __init__(self):
    #     self.prices = []
    #     self.spans = []

    # def next(self, price: int) -> int:
    #     if self.prices:
    #         if price >= self.prices[-1]:
    #             i = self.spans[-1]
    #             while i <= len(self.prices) and self.prices[-i] <= price:
    #                 i += 1
    #             self.prices.append(price)
    #             self.spans.append(i)
    #             return i
    #     self.prices.append(price)
    #     self.spans.append(1)
    #     return 1