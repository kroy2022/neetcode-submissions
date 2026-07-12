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
            needed = 0 - nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                if l == i:
                    l += 1
                    continue
                elif r == i:
                    r -= 1
                    continue

                currSum = nums[l] + nums[r]
                if currSum == needed and [nums[i], nums[l], nums[r]] not in res:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                elif currSum < needed:
                    l += 1
                else:
                    r -= 1

        return res










        
            
