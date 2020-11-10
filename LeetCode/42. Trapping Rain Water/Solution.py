class Solution:
    def trap(self, height: List[int]) -> int:
        size = 0
        length = len(height)
        
        for i in range(length):
            leftMax = 0
            rightMax = 0
            
            for j in range(i, -1, -1):
                leftMax = max(leftMax, height[j])
            
            for j in range(i, length):
                rightMax = max(rightMax, height[j])
            
            size += min(leftMax, rightMax) - height[i]
        
        return size
