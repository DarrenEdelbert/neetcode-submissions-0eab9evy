class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                print(i)
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                print(i)
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)     
            elif i == "*":
                print(i)
                stack.append(stack.pop() * stack.pop())
            elif i == "/":
                print(i)
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a)) #int to round off towards 0. // doesnt work
            else:
                stack.append(int(i))
                print(stack)
        return stack[0]
