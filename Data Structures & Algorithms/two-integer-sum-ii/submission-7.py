class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        numbers = [1,2,3,4], target = 3

        l = 0
        r = 1
        num = 3
        """
        L, R = 0, len(numbers) - 1
        while L < R:
            curr = numbers[L] + numbers[R]
            if curr > target:
                R -= 1
            elif curr < target:
                L += 1
            else:
                return [L+1, R+1]
        
        
