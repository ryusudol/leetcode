class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            return True if flowerbed[0] == 0 or (flowerbed[0] == 1 and n == 0) else False
        count = 0
        for idx, p in enumerate(flowerbed):
            if p == 0:
                if (idx == 0 and flowerbed[idx + 1] == 0) or (idx == len(flowerbed) - 1 and flowerbed[idx - 1] == 0) or (flowerbed[idx - 1] == 0 and flowerbed[idx + 1] == 0):
                    flowerbed[idx] = 1
                    count += 1
        return True if count >= n else False