class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        prev = nums[0]
        count = 1
        res = 1
        for i in range(1,len(nums)): 
            if nums[i]-prev == 1:
                prev = nums[i]
                count += 1
                if count>res:
                    res = count
            elif nums[i]-prev == 0:
                continue
            else:
                if count>res:
                    res = count
                count = 1
                prev = nums[i]
        return res
