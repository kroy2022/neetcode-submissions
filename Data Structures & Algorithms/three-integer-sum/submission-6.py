class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        - Sort the array
        - Use left pointer and right pointer elements and create target
        - Binary search inside loop looking for value

        nums = [-1,0,1,2,-1,-4]
        needed = -5
        """
        nums.sort()
        res = []

        for i in range(len(nums)):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # When entering this loop i != l != r and they are NOT duplicates
            l, r = i + 1, len(nums) - 1
            while l < r:
                curSum = nums[i] + nums[l] + nums[r]
                if curSum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1  

                    # Don't check numbers that have been checked
                    while l < len(nums) and nums[l] == nums[l-1]:
                        l += 1
                    while r > -1 and nums[r] == nums[r+1]:
                        r -= 1

                elif curSum < 0:
                    l += 1
                else:
                    r -= 1
        return res








        
            
