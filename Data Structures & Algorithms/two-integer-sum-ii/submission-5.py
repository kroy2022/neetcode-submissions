class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}

        for i in range(len(numbers)):
            goal = target - numbers[i]

            if goal in dic:
                return [dic[goal] + 1, i + 1]
            
            dic[numbers[i]] = i
        
        