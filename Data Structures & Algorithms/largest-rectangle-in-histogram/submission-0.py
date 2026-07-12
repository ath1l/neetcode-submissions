class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        rb = [0]* len(heights) #rightboundary
        lb = [0]* len(heights) #leftboundary
        stack = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                rb[stack.pop()] = i
            stack.append(i)
        while stack:
            rb[stack.pop()] = len(heights)

        for i in range(len(heights)-1,-1,-1):
            while stack and heights[stack[-1]] > heights[i]:
                lb[stack.pop()] = i
            stack.append(i)
        while stack:
            lb[stack.pop()] = -1

        ans = 0
        for i in range(len(heights)):
            height = heights[i]
            breadth = rb[i] - lb[i] -1
            area = breadth * height
            if area>ans:
                ans = area
        return ans       