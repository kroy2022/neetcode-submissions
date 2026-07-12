class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i in range(len(nums)):
            goal = target - nums[i]

            if goal in dic:
                return [dic[goal], i]
            
            dic[nums[i]] = i
        
