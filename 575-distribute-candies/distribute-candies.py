class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candyType.sort()
        candy_basket = {}
        candy_kinds = 0
        for candy in candyType:
            if candy not in candy_basket:
                candy_basket[candy] = True
                candy_kinds += 1
        if len(candyType) // 2 >= candy_kinds:
            return candy_kinds
        else:
            return len(candyType) // 2