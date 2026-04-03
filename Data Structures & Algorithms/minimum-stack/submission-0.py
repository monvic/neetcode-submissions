class MinStack:

    def __init__(self):
        self.stack = []
        # self.m = float('-inf')
        self.mStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if self.mStack:
             self.mStack.append(min(val,self.mStack[-1]))
        else:
            self.mStack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.mStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.mStack[-1]

        
