class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # car b = speed2 pos4
        # targ = 10
        # steps = 10 - 4/2 ((targ - pos)/speed)
        # calculate steps for every car and add it to the stack
        # if the current car will reach the target in fewer steps 
        # than the car in front of it, it will be part of a fleet
        
        pair = [[p,s] for p,s in zip(position, speed)]
        print(pair)
        stack = []
        for p,s in sorted(pair)[::-1]:
            stack.append((target - p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
            