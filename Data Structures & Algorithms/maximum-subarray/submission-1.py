class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        nums = [2,-3,4,-2,2,1,-1,4]

        curSum = 4
        maxSum = 4
        """
        maxSum = nums[0]
        curSum = 0

        for num in nums:
            curSum = max(curSum, 0)
            curSum += num
            maxSum = max(curSum, maxSum)
        
        return maxSum
        