class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        s = "AAABABB", k = 1
        mostFreq = {
            A: 2
            B: 3
        }
        longest = 5
        R = 6
        L = 2
        mostApps = 3
        windowSize = 6
        """
        longest, tempLongest = 0, 0
        mostApps = 0
        mostFreq = {}
        L = 0
        for R in range(len(s)):
            if s[R] in mostFreq:
                mostFreq[s[R]] += 1
            else:
                mostFreq[s[R]] = 1
            
            for value in mostFreq.values():
                mostApps = max(value, mostApps)
            
            windowSize = (R - L) + 1
            if k >= (windowSize - mostApps):
                longest = max(longest, windowSize)
            else:
                mostFreq[s[L]] -= 1
                L += 1
        
        return longest