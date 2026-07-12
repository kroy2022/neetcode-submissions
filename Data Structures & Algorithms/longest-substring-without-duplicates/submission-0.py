class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        zxyzxyz

        tempString = yzx
        """

        length = 0
        tempString = ""
        for c in s:
            while c in tempString:
                tempString = tempString[1:]
            
            tempString += c
            length = max(length, len(tempString))

        return length
