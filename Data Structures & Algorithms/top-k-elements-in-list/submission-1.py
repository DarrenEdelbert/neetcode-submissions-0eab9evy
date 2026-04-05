class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for i in nums:
            if i in hmap:
                hmap[i] += 1
            else:
                hmap[i] = 1
        sorted_hmap = dict(sorted(hmap.items(), key=lambda item: item[1], reverse=True))
        print(sorted_hmap)

        res = []
        for i in sorted_hmap:
            print(i)
            if len(res) == k:
                break
            res.append(i)
        return res
