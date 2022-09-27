class MinStack:

    def __init__(self):
        self.stck = []
        self.minstk = []
        

    def push(self, val: int) -> None:
        self.stck.append(val)
        if len(self.minstk) == 0:
            self.minstk.append(val)
        else:
            self.minstk.append(min(val, self.minstk[-1]))
        

    def pop(self) -> None:
        self.stck.pop()
        self.minstk.pop()

    def top(self) -> int:
        return self.stck[-1]

    def getMin(self) -> int:
        return self.minstk[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()