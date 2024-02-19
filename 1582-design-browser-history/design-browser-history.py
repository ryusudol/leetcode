class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.history = [homepage]
        self.curr_idx = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.curr_idx + 1]
        self.history.append(url)
        self.curr_idx = len(self.history) - 1

    def back(self, steps: int) -> str:
        self.curr_idx -= steps
        if self.curr_idx < 0:
            self.curr_idx = 0
        return self.history[self.curr_idx]

    def forward(self, steps: int) -> str:
        self.curr_idx += steps
        if self.curr_idx >= len(self.history):
            self.curr_idx = len(self.history) - 1
        return self.history[self.curr_idx]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)