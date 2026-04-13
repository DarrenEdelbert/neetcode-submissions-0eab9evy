class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = [] # this stack will hold the smallest value in every position, 
        # so even if one element is popped, 
        # it will have the smallest element of the current elements at the top

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minstack[-1] if self.minstack else val) #in case stack is empty
        self.minstack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack = self.stack[:len(self.stack)-1]
            self.minstack = self.minstack[:len(self.minstack)-1]

    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.minstack[-1]
        
        
