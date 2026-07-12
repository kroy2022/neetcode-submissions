class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Input: target = 10, nums = [2,1,5,1,5,3]

        length = 3
        curSum = 9
        R = 5
        L = 3
        """
        length = len(nums) + 1
        curSum = 0
        L = 0
        for R in range(len(nums)):
            curSum += nums[R]
            while curSum >= target:
                length = min(length, R - L + 1)
                curSum -= nums[L]
                L += 1
        
        if length == len(nums) + 1:
            return 0
        
        return length