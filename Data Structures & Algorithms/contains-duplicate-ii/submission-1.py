class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        [2,1,2]
        k = 2

        i = 2
        window = {2,1}
        """
        window = set()

        for i in range(len(nums)):
            if nums[i] in window:
                return True
            
            window.add(nums[i])
            
            if len(window) > k:
                window.remove(nums[i - k])
            
        return False
