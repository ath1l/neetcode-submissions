class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        for i in range(len(heights)):
            for j in range(len(heights)-1,i,-1):
                if heights[i] < heights[j]:
                    length = heights[i]
                else:
                    length = heights[j]
                breadth = j-i
                if max < length*breadth:
                   max = length*breadth
        return max