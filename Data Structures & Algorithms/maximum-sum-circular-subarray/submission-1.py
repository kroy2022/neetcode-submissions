class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        - Calculate global max, min, and sum
        - Return the max between the global max OR sum - global min
        - EDGE CASE: if global max is negative just return that
        """
        minSum, maxSum = nums[0], nums[0]
        totalSum, curMax, curMin = 0, 0, 0
        for i in range(len(nums)):
            # find local max
            if curMax < 0:
                curMax = 0
            #find local min
            if curMin > 0:
                curMin = 0

            curMax += nums[i]
            curMin += nums[i]
            maxSum = max(maxSum, curMax)
            minSum = min(minSum, curMin)
            totalSum += nums[i]
        
        if maxSum < 0:
            return maxSum

        return max(maxSum, (totalSum - minSum))



        
