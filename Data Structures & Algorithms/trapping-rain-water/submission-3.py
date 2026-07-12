class Solution:
    def trap(self, height: List[int]) -> int:
        """
        height = [0,2,0,3,1,0,1,3,2,1]
        

        """
        maxLeft = [0]
        prevMax = 0
        for i in range(1, len(height)):
            prevMax = max(prevMax, height[i-1])
            maxLeft.append(prevMax)
        
        minNums = [0] * len(height)
        prevMax = 0
        for i in range(len(height)-2, -1, -1):
            prevMax = max(prevMax, height[i+1])
            minNums[i] = min(prevMax, maxLeft[i])
        
        maxWater = 0
        for i in range(len(height)):
            curSum = max(0, minNums[i] - height[i])
            maxWater += curSum
        
        return maxWater