class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        i = 0
        j = len(heights)-1
        while i<j:
            if heights[i]<=heights[j]:
                length = heights[i]
                breadth = j-i
                i+=1
            else:
                length = heights[j]
                breadth = j-i
                j-=1
            area = length*breadth
            if area>max:
                max = area
        return max
            