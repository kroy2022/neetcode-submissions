class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0] * len(height)
        max_right = [0] * len(height)

        max_left[0] = height[0]
        for i in range(1, len(height)):
            max_left[i] = max(max_left[i-1], height[i])

        max_right[len(height) - 1] = height[len(height) - 1]
        for i in range(len(height) - 2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i])

        max_water = 0
        for i in range(1, len(height)):
            max_water += max(min(max_left[i], max_right[i]) - height[i], 0)
        
        return max_water
            
        

