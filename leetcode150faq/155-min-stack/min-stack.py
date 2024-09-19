class MinStack:

    def __init__(self):
        self.stk = []
        self.min_stk = []
        
    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.min_stk or self.min_stk[-1] > val:
            self.min_stk.append(val)
        else:
            self.min_stk.append(self.min_stk[-1])
    
    def pop(self) -> None:
        self.min_stk.pop()
        self.stk.pop()    

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min_stk[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()