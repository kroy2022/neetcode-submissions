class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Approach:
        - 
        """
        arr = [0] * len(nums)
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                product *= nums[j]
            
            arr[i] = product
        
        print(arr)
        return arr

