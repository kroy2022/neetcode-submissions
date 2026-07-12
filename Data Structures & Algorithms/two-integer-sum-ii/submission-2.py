class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        dic = { num : index }

        """
        dic = {}
        for i in range(len(numbers)):
            hit = target - numbers[i]
            if hit in dic:
                return [dic[hit], i + 1]
            
            dic[numbers[i]] = i + 1
        