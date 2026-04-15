class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # SOLVED THIS BY MYSELF RAHHHHH
        # Used a monotonic stack (in decreasing order)
        stack = []
        res = [0]*len(temperatures)
        for i, t in enumerate(temperatures):
            stack.append((t,i))
            # for every new item in the stack, 
            # we pop all smaller elements and calculate the number of days using index
            # stack[(len(stack)-2)][0] -> this will get the topmost temperature in the stack (excluding 
            # the one we just appended to the stack)
            while stack and t > stack[(len(stack)-2)][0]:
                res[stack[(len(stack)-2)][1]] = i - stack[(len(stack)-2)][1]
                stack.pop(len(stack)-2)
            
        return res
        



# thinking
# [30,38,30,36,35,40,28]

# if new element bigger than previous, pop previous element and calculate distance
# use while loop
#     28, 6
#     40, 5
#     35, 4
#     36, 3
#     30, 2
#     38, 1
#     30, 0 - pop (do 1 - 0 to get ans)