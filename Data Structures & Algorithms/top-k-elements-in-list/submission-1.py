class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}

        for num in nums:
                mp[num] = mp.get(num,0) + 1
        
        sorted_items = sorted(mp.items(),key = lambda x: x[1],reverse = True)
    
        result = []
        for i in range(k):
                result.append(sorted_items[i][0])
        return result

