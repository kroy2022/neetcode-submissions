class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        [2,1,2]
        k = 1

        i = 2
        index = 0
        dupMap = {
            2: 0,
            1: 1
        }
        """
        dupMap = {}
        for i in range(len(nums)):
            if nums[i] in dupMap:
                index = dupMap[nums[i]]
                if i - index <= k:
                    return True
            
            dupMap[nums[i]] = i
        
        return False

