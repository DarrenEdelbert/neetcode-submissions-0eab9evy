class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        vol = 0
        while l<r:
            vol = max(vol, (min(heights[l],heights[r]) * (r-l)))
            print("L,R,V", heights[l], heights[r], vol)
            if heights[l]<heights[r]:
                l+=1
            elif heights[l]>heights[r]:
                r-=1
            else: 
                r-=1
        return vol
            

        # height and distance matters