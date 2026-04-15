class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for i, t in enumerate(temperatures):
            # if not stack:
            #     stack.append((t,i))
            #     continue
            # if t <= stack[(len(stack)-1)][0]:
            #     stack.append((t,i))
            #     print(stack)
            stack.append((t,i))
            while stack and t > stack[(len(stack)-2)][0]:
                print("in while")
                print(stack)
                a = stack[(len(stack)-2)][1]
                res[a] = i - a
                b = len(stack)-2
                stack.pop(b)
            
        return res
        




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