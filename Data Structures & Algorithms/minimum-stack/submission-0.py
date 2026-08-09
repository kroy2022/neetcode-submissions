class MinStack:
    def __init__(self):
        self.stack = []
        self.sortedStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.sortedStack) == 0 or val < self.sortedStack[-1]:
            self.sortedStack.append(val)
        else:
            self.sortedStack.append(self.sortedStack[-1])


    def pop(self) -> None:
        self.val = self.stack.pop(-1)
        self.sortedStack.pop(-1)


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.sortedStack[-1]
