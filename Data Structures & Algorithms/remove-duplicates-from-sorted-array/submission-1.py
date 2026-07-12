class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lastSeen = None
        L = 0
        for R in range(len(nums)):
            if nums[R] != lastSeen:
                lastSeen = nums[R]
                curr = nums[L]
                nums[L] = nums[R]
                nums[R] = curr
                L += 1
        
        return L