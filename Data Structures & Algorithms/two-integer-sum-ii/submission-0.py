class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        numbers = [1,3,4,8], target = 7
                     | |
        """
        p1, p2 = 0, len(numbers) - 1
        #i = 0,1,2,3
        for i in range(len(numbers)):
            if numbers[p1] + numbers[p2] < target:
                p1 += 1
            elif numbers[p1] + numbers[p2] > target:
                p2 -= 1
            else: 
                return [p1 + 1, p2 + 1]


        