class SmallestInfiniteSet:

    def __init__(self):
        self.arr = [i + 1 for i in range(1000)]

    def popSmallest(self) -> int:
        return heappop(self.arr)

    def addBack(self, num: int) -> None:
        if num not in self.arr:
            heappush(self.arr, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)