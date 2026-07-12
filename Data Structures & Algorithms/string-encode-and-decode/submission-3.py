class Solution:
    """
    Initial Approach: 
        - Add the length of the word and then a hashtag 

    Clarifying:
        - If a hashtag is part of the input string we get an issue
        - Can string be a number?

    4neet4code4love3you
    """
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + "#" + string

        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            decoded.append(s[j+1:length+j+1])
            i = length + j + 1
            
        return decoded
            
        
        return decoded