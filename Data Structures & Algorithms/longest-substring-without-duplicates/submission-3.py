class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        substring = set()

        for i in range(len(s)):
            while s[i] in substring:
                substring.remove(s[l])
                l += 1

            substring.add(s[i])
            longest = max(longest, len(substring))
        
        return longest
            
