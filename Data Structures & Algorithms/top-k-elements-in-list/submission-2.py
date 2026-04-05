class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # created a dictionary {number: count} and then sorted it in desc order, 
        # then returned a list of the top k freq
        hmap = {}
        for i in nums:
            if i in hmap:
                hmap[i] += 1
            else:
                hmap[i] = 1
        sorted_hmap = dict(sorted(hmap.items(), key=lambda item: item[1], reverse=True)) #IMPORTANT

        res = []
        for i in sorted_hmap:
            if len(res) == k:
                break
            res.append(i)
        return res
