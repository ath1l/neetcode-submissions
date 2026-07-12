class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0]*len(height)
        max = height[0]
        for i in range(1,len(height)):
            maxLeft[i] = max
            if height[i] > max:
                max = height[i]
            
        maxRight =[0]*len(height)
        max = height[-1]
        for i in range(len(height)-2,-1,-1):
            maxRight[i] = max
            if height[i] >max:
                max =height[i]
            
        res = 0
        for i in range(len(height)):
            w = min(maxLeft[i],maxRight[i]) - height[i]
            if w > 0:
                res += w
        return res
                

                    