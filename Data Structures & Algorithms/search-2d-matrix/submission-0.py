class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flattened = [item for sublist in matrix for item in sublist]
        s,e = 0, len(flattened)-1
        while s <= e:
            mid = s + (e-s)//2
            if flattened[mid] == target:
                return True
            elif flattened[mid] < target:
                s = mid+1
            else:
                e = mid-1
        return False