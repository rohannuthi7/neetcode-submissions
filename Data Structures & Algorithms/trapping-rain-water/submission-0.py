class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        leftBarrier = height[left]
        rightBarrier = height[right]
        total = 0

        while left < right:
            if leftBarrier < rightBarrier:
                left += 1
                leftBarrier = max(height[left],leftBarrier)
                total += leftBarrier - height[left]
            else:
                right -= 1
                rightBarrier = max(height[right],rightBarrier)
                total += rightBarrier - height[right]
        
        return total