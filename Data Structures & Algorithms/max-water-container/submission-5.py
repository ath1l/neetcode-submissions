class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        water = 0
        while left<right:
            wall = min(heights[left],heights[right])
            if water<wall*(right-left):
                water = wall*(right-left)
            if heights[left] <= heights[right]:
                left+=1
            else:
                right-=1
        return water