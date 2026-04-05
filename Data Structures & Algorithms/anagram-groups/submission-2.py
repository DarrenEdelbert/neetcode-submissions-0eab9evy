class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]

        hmap = defaultdict(list)
        for str in strs:
            count = [0] * 26 #array of 26 0s - for every letter (basically for one hot encoding)

            for i in str:
                count[ord(i) - ord("a")] += 1
            hmap[tuple(count)].append(str)
        
        return list(hmap.values())
