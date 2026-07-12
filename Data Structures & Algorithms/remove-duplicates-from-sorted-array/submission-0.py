class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        nums = [1,1,2,3,4]

        seen = {
            1: 0
            2: 2
            3: 3
            4: 4
        }
        nums = [1,2,3,4,1]
        L = 4
        R = 4
        """
        seen = {}
        L = 0
        for R in range(len(nums)):
            if nums[R] not in seen:
                seen[nums[R]] = R
                curr = nums[L]
                nums[L] = nums[R]
                nums[R] = curr
                L += 1
        
        return L