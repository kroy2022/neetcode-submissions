class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        [-2,4,-5,4,-5,9,4]

        curSum = 2
        maxSum = 2
        """
        curMaxSum, curMinSum = 0, 0
        maxSum = nums[0]
        minSum = nums[0]
        totalSum = 0

        for num in nums:
            totalSum += num
            curMaxSum = max(curMaxSum, 0)
            curMinSum = min(curMinSum, 0)
            curMaxSum += num
            curMinSum += num
            maxSum = max(curMaxSum, maxSum)
            minSum = min(curMinSum, minSum)

        circular_max = totalSum - minSum
        if circular_max == 0:
            return maxSum

        return max(maxSum, circular_max)