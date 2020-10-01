class RecentCounter:

    def __init__(self):
        self.res = []

    def ping(self, t: int) -> int:
        self.res.append(t)
        while self.res[0]<self.res[-1] - 3000:
            self.res.pop(0)
        return len(self.res)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
