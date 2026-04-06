class Solution:
    def isPalindrome(self, s: str) -> bool:
        # EASY
        # ss = ''
        # for c in s:
        #     if c.isalnum():
        #         ss += c.lower()

        # return ss[::-1]==ss

        # TWO POINTER:
        l, r = 0, len(s)-1
        s = s.lower()
        while l<r:
            while l<r and not s[l].isalnum():
                l += 1
            while l<r and not s[r].isalnum():
                r -= 1
            print(f"{s[l]}, {s[r]}")
            if s[l] == s[r]:
                l+=1
                r-=1
            elif s[l] != s[r]:
                return False
        return True  
