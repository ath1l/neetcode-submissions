class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hMap = {}
        for i in range(len(nums)):
                    complement = target - nums[i] 
                    if complement in hMap:
                        return [hMap[complement],i]
                    hMap[nums[i]] = i
                   