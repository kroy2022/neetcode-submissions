class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        height = [1,7,2,5,4,7,3,6]

        R = 6
        L = 1
        amount = 36
        currAmount = 36
        """
        amount = 0
        L, R = 0, len(heights) - 1  
        while L < R:
            currAmount = min(heights[L], heights[R]) * (R - L)
            amount = max(amount, currAmount)

            if heights[L] <= heights[R]:
                L += 1
            else:
                R -= 1
        
        return amount