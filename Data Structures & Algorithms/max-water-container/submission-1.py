class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        result = 0
        while left < right:
            if heights[left] <= heights[right]:
                result = max((right-left) * heights[left], result)
                left += 1
            else:
                result = max((right-left) * heights[right], result)
                right -= 1
                
        return result