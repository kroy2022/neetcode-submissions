class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        - Keep a curSum, maxSum, l pointer, r pointer variable 
        - Iterate over nums with l and r being start and end of current 
        window respectfully
        - if curSum goes negative move l = r and curSum = 0 (reset window)
        - Check maxSum every iteration
        """
        l = 0
        curSum = 0
        maxSum = nums[0]
        for r in range(len(nums)):
            if curSum < 0:
                curSum = 0
                l = r
            
            curSum += nums[r]
            maxSum = max(curSum, maxSum)
        
        return maxSum