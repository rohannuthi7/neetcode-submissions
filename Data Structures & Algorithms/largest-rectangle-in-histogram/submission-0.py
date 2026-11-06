class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                index = stack.pop()
                width = i - stack[-1] - 1 if stack else i
                area = width * heights[index]
                if area > maxArea:
                    maxArea = area
            stack.append(i)

        while stack:
            index = stack.pop()
            width = len(heights) - stack[-1] - 1 if stack else len(heights)
            area = width * heights[index]
            if area > maxArea:
                maxArea = area

        return maxArea