class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # BRUTE FORCE
        # for i in range(len(numbers)-1):
        #     for j in range(i+1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1,j+1]

        for i in range(len(numbers)):
            l,r = i+1, len(numbers)-1
            temp = target - numbers[i]
            while l<=r:
                mid = l + (r-l)//2
                if numbers[mid] == temp:
                    return [i+1,mid+1]
                elif numbers[mid] > temp:
                    r = mid-1
                elif numbers[mid] < temp:
                    l = mid+1
        return []