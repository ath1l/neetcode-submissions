class Solution:
        def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            mp = {}
            for num in nums:
                mp[num] = mp.get(num,0) + 1
            arr = [[] for i in range(len(nums)+1)]
            for key,value in mp.items():
                arr[value].append(key)
            result = []
            for i in range(len(nums),0,-1):
                if arr[i]:
                    for num in arr[i]:
                        result.append(num)
                        if len(result) == k:
                            return result



