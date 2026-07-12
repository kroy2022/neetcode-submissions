class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights) - 1

        max_water = float("-inf")
        while l < r:
            val = min(heights[l], heights[r])
            max_water = max(max_water, val * (r - l)) 
            
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return max_water