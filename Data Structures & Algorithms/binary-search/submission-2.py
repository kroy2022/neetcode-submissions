class Solution:
    """
    nums = [-1,0,2,4,6,8], target = 3
    l = 3
    r = 5
    mid = 2
    curNum = 0
    """
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (r + l) // 2
            print(mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1