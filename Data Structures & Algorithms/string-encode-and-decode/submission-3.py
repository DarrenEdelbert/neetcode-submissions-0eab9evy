class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        print(res)
        return res
    
    def decode(self, s: str) -> List[str]:
        res = []
        tracker = 0
        while tracker < len(s):
            hash_index = tracker
            while s[hash_index] != "#":
                hash_index += 1
            length = int(s[tracker:hash_index])
            res.append(s[hash_index+1: hash_index+1+length])
            tracker = hash_index+1+length
        return res
        

    # MY SOLUTION: DIDNT ACTUALLY HAVE TO IMPLEMENT ANY KIND OF ENCRYPTION - PASSED 42/51 TESTCASES
    # def encode(self, strs: List[str]) -> str:
    #     res = []
    #     for str in strs:
    #         a = []
    #         for i in range(len(str)):
    #             a.append(chr(ord(str[i])+3))
    #         res.append(''.join(a))
    #         res.append('.')
    #     print(res)
    #     return ''.join(res)

    # def decode(self, s: str) -> List[str]:
    #     res = []
    #     a = []
    #     for c in s:
    #         if c!='.':
    #             a.append(chr(ord(c)-3))
    #         else:
    #             res.append(''.join(a))
    #             a = []
    #     print(res)
    #     return res
