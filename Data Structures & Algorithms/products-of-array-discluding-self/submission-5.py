class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Input: nums = [-1,0,1,2,3] => 5
        Output: [0,-6,0,0,0]

        [1, -1, 0, 0, 0, 0] =? 6 - 1 => 5
        [0, 0, 6, 6, 3, 1]
        i = 5
        output = [0, -6, 0, 0, 0]
        """
        prefix = [1] * (len(nums) + 1)
        postfix = [1] * (len(nums) + 1)

        for i in range(len(nums)):
            prefix[i+1] = prefix[i] * nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            postfix[i] = postfix[i+1] * nums[i]
        
        output = []
        for i in range(len(prefix)-1):
            output.append(prefix[i] * postfix[i+1])
        
        return output


        

