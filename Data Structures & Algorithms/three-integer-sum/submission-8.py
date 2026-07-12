class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Input: nums = [-1,0,1,2,-1,-4]
        i = 1
        j = 0
        combinations = []
        goal = 0
        target = 
        """
        combinations = []
        for i in range(len(nums)):
            goal = 0 - nums[i]
            seen = set()

            for j in range(i):
                target = goal - nums[j]

                if target in seen:
                    sorted_list = sorted([nums[i], target, nums[j]])
                    if sorted_list not in combinations:
                        combinations.append(sorted_list)
                
                seen.add(nums[j])
        
        return combinations