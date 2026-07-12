class Solution:
    """
    target = 7
    [3,4,5,6]
    {
        3: 0
    }
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dic:
                return [dic[diff], i]
            
            dic[nums[i]] = i
        
        