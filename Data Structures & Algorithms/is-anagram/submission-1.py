class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        r_hash = {}
        for i in s:
            if i in s_hash:
                s_hash[i] += 1
            else:
                s_hash[i] = 1

        for i in t:
            if i in r_hash:
                r_hash[i] += 1
            else:
                r_hash[i] = 1

        return s_hash == r_hash