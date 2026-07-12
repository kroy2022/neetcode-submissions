class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        s = "zxyzxyz"

        set = (xyz)  
        """
        longest = 0
        substring = ""
        for c in s:
            while c in substring:
                substring = substring[1:]

            substring += c
            longest = max(longest, len(substring))
        
        return longest
            
