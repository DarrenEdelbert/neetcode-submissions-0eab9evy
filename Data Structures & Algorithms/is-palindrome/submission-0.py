class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ''
        for c in s:
            if c.isalnum():
                ss += c.lower()
        if ss[::-1]==ss:
            return True
        else: return False
