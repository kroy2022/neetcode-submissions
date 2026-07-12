class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        """
        l = 0
        r = len(numbers) - 1
        for i in range(len(numbers)):
            needed = target - numbers[i]
            while l < r:
                if needed == numbers[l]:
                    return [min(l+1, i+1), max(i+1, l+1)]
                elif needed == numbers[r]:
                    return [min(r+1, i+1), max(i+1, r+1)]
                elif needed > numbers[l]:
                    l += 1
                else:
                    r -= 1
            l = 0
            r = len(numbers) - 1

        