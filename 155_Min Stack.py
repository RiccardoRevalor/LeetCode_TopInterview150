class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None
        

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.min = val
        else:
            if val < self.min: self.min = val
        self.stack.append(val)
        

    def pop(self) -> None:
        if self.stack[-1] == self.min:
            #update minimum
            self.stack.pop(-1)
            if len(self.stack) > 0:
                self.min = min(self.stack)
            else: self.min = None #if now the stack is empty there's no minimum
            return
        self.stack.pop(-1)
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
