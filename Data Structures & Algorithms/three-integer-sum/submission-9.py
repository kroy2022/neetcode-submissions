class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        combinations = set()
        for i in range(len(nums)):
            goal = 0 - nums[i]
            seen = set()

            for j in range(i):
                target = goal - nums[j]

                if target in seen:
                    sorted_tuple = tuple(sorted([nums[i], target, nums[j]]))
                    if sorted_tuple not in combinations:
                        combinations.add(sorted_tuple)
                                    
                seen.add(nums[j])
        
        return list(combinations)