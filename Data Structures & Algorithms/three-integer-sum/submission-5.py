class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        i = 0
        while i<len(nums)-2:
            j = i+1
            k =len(nums)-1
            while j<k:
                if nums[i]+nums[j]+nums[k] == 0:
                    if [nums[i],nums[j],nums[k]] not in res:
                        res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                elif nums[i]+nums[j]+nums[k] < 0:
                    j+=1
                else:
                    k-=1
            i+=1
        return res
            
                
