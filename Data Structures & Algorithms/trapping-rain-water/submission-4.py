class Solution:
    def trap(self, height: List[int]) -> int:
        """
        height = [0,2,0,3,1,0,1,3,2,1]

        R = 7
        L = 7
        maxRight = 2
        maxLeft = 3
        totalWater = 9
        """
        L, R = 0, len(height) - 1
        totalWater = 0
        maxLeft = 0
        maxRight = 0
        while L < R:
            if height[L] <= height[R]:
                totalWater += max(0, maxLeft - height[L])
                maxLeft = max(maxLeft, height[L])
                L += 1
            else:
                totalWater += max(0, maxRight - height[R])
                maxRight = max(maxRight, height[R])
                R -= 1
        
        return totalWater
