class Solution:
    """
    s = "[(])"
    seen = [[,]
    c = ]
    char = (
    """
    def isValid(self, s: str) -> bool:
        dic = {
            "]": "[",
            ")": "(",
            "}": "{"
        }
        seen = []

        for c in s:
            if c in dic:
                if len(seen) == 0:
                    return False
                
                char = seen.pop(-1)
                if char != dic[c]:
                    return False
            else:
                seen.append(c)
        
        return len(seen) == 0

