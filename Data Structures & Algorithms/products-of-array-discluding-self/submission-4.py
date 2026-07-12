class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        nums=[1,2,4,6]
        arr=[1,1,2,8]
        postfix_arr = [1,32,16,8]
        postfix = 64
        j = 0
        """
        arr = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            arr[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for j in range(len(nums)-1,-1,-1):
            arr[j] *= postfix
            postfix *= nums[j]
        return arr