class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()
        print(nums)
        for i, n in enumerate(nums):
            #once our loop exits the negative part of our array, 
            # all the following numbers will lead to a sum greater than 0 -> so no point
            if n > 0: 
                break

            if i > 0 and n == nums[i-1]: # skip if the current element is the same as the previous one
                continue
            l,r = i+1, len(nums)-1
            while l < r:
                add = n + nums[l] + nums[r]
                if add < 0:
                    l += 1
                elif add > 0:
                    r -= 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1

                    while nums[l] == nums[l-1] and l<r: #keep skipping if the next element is a duplicate of the current one
                        l+=1 
                    
        return res
