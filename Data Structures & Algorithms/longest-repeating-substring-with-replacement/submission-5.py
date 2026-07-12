class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest, tempLongest = 0, 0
        mostFreq = {}
        mostApps = 0
        L = 0
        for R in range(len(s)):
            if s[R] in mostFreq:
                mostFreq[s[R]] += 1
            else:
                mostFreq[s[R]] = 1
                        
            mostApps = max(mostFreq[s[R]], mostApps)
            
            while k < ((R - L) + 1 - mostApps):
                mostFreq[s[L]] -= 1
                L += 1
            
            longest = max(longest, (R - L) + 1)
        
        return longest