class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]

        hmap = defaultdict(list)
        # Why do we need defaultdict()
        # In a normal dictionary, accessing a missing key raises a KeyError. 
        # In this problem, we might try to append a value to a key that doesnt exist
        # defaultdict solves this by: Automatically creating missing keys with a default value.
        for str in strs:
            count = [0] * 26 #array of 26 0s - for every letter (basically for one hot encoding)

            for i in str:
                count[ord(i) - ord("a")] += 1 #ord returns ASCII value
            hmap[tuple(count)].append(str)
        
        return list(hmap.values())
