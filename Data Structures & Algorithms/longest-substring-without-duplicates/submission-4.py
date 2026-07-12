class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        s = "xxxx"

        dupSet = {x}
        length = 1
        R = 0
        L = 0
        """
        dupSet = set()
        length = 0
        L = 0
        for R in range(len(s)):
            while s[R] in dupSet:
                dupSet.remove(s[L])
                L += 1
            
            dupSet.add(s[R])
            length = max(length, len(dupSet))
        
        return length