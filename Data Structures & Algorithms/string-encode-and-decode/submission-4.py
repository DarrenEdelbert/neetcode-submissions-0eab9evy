class Solution:

    def encode(self, strs: List[str]) -> str:
        # append the length of each string and # before the actual string -> acts as the delimiter
        # and tells us how long the text is
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s 
        print(res)
        return res
    
    def decode(self, s: str) -> List[str]:
        res = []
        tracker = 0 #track where we are at in the encoded string
        while tracker < len(s):
            hash_index = tracker # hash_index tells me where the hashtag is
            while s[hash_index] != "#":
                hash_index += 1
            length = int(s[tracker:hash_index]) #tracker:hash_index -> helps me single out the number before the hashtag
            res.append(s[hash_index+1: hash_index+1+length]) #append the actual string that comes after the hashtag and before the next delimiter
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
