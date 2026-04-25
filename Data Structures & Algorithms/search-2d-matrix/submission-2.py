class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # i = [item for sublist in matrix for item in sublist]
        for i in matrix:
            if target > i[-1]: #since the matrix is sorted, no need to look for the target in this array if the target is greater than the last element
                continue

            s,e = 0, len(i)-1
            while s <= e:
                mid = s + (e-s)//2
                if i[mid] == target:
                    return True
                elif i[mid] < target:
                    s = mid+1
                else:
                    e = mid-1
        return False