class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = []
        for c in s:
            if c.isalnum():
                new_s.append(c.upper())
        
        new_s = "".join(new_s)
        return new_s == new_s[::-1]