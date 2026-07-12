class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        - Two pointer approach
        - val = min(l , r)
        - get the area = val^2
        - if num @ l < num @ r: l ++
        - else
        """
        l, r = 0, len(heights) - 1
        maxArea = float("-inf")
        while l < r:
            maxArea = max(min(heights[l], heights[r]) * (r-l), maxArea)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea