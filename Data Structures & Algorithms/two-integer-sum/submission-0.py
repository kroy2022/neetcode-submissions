class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        nums = [3,4,5,6], target = 11

        hashmap:
        {
            (11-3)=8 : 0
            (11-4)=7 : 1
            (11-5)=6 : 2
            
        }
        """

        dic = {}
        # 0 - 4 or 0 - 3 index
        for index, val in enumerate(nums):
            if val not in dic:
                dic[target - val] = index
            else:
                return [dic[val], index]