class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

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
        # smin = self.stack[0]
        # for i in self.stack:
        #     smin = min(smin,i)
        return self.minstack[-1]
        
        
