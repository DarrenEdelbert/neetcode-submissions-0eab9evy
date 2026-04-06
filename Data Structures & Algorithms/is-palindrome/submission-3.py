class Solution:
    def isPalindrome(self, s: str) -> bool:
        # TWO POINTER:
        l, r = 0, len(s)-1
        s = s.lower()
        while l<r:
            while l<r and not s[l].isalnum(): # keep moving till you find a non alphanumeric character
                l += 1
            while l<r and not s[r].isalnum(): # keep moving till you find a non alphanumeric character
                r -= 1
            if s[l] == s[r]:
                l+=1
                r-=1
            elif s[l] != s[r]:
                return False
        return True


        # EASY
        # ss = ''
        # for c in s:
        #     if c.isalnum():
        #         ss += c.lower()

        # return ss[::-1]==ss

