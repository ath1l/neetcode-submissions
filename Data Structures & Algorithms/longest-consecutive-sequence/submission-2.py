class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        res = sorted(nums)
        count = maxLen = 1
        for i in range(1,len(res)):
            if res[i] == res[i-1]:
                continue
            if res[i]-res[i-1] == 1:
                count += 1
            else:
                count = 1
            if count>maxLen:
                    maxLen = count
        return maxLen