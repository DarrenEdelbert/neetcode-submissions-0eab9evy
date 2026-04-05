class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = len(nums)
        b = len(set(nums))
        if a == b:
            return False
        else: return True