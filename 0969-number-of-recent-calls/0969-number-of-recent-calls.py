class RecentCounter:

    def __init__(self):
        self.pings = [0] * 10000
        self.l = 0
        self.r = 0

        # My First Approach
        # self.pings = []

    def ping(self, t: int) -> int:
        while self.l < self.r and self.pings[self.l] < t - 3000:
            self.l += 1
        self.pings[self.r] = t
        self.r += 1
        return self.r - self.l
        
        # My First Approach
        # count = i = 0
        # while len(self.pings) > i and self.pings[-1 - i] >= t - 3000:
        #     count += 1
        #     i += 1
        # return count


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)