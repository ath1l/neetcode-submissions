class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [0]*n
        right = [0]*n
        res = [0]*n
        left[0] = nums[0]
        for i in range(1,n):
            left[i] = left[i-1]*nums[i]
        print(left)
        right[n-1] = nums[n-1]
        for i in range(n-2,-1,-1):
            right[i] = right[i+1]*nums[i]
        print(right)
        for i in range(n):
            if i == 0:
                res[i] = right[i+1]
            elif i== n-1:
                res[i] = left[i-1]
            else:
                res[i]=left[i-1]*right[i+1]
        return res