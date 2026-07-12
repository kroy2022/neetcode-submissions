class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {}

        for i, curr in enumerate(nums):
            diff = target - curr
            if diff in dic:
                return [dic[diff], i]
            dic[curr] = i