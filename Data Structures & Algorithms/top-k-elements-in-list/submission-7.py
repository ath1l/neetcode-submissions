class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        res = []
        for num in nums:
                mp[num] = mp.get(num,0) + 1
        print(mp)
        sorted_items = sorted(mp.items(),key=lambda x:x[1],reverse = True)
        print(sorted_items)
        for num,freq in sorted_items[:k]:
            res.append(num)
        return res