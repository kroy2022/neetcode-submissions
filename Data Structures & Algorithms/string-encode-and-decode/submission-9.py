class Solution:
    """
    ["neet","code","love","you"]
    neetcodiet10$code4$love4$you3$
    """
    def encode(self, strs: List[str]) -> str:
        output = []
        for s in strs:
            output.append(f"{str(len(s))}${s}")
        
        return "".join(output)

    def decode(self, s: str) -> List[str]:
        # 4$neet4$code4$love3$you
        l, r = 0, 0
        decoded = []
        while r < len(s):
            while s[r] != "$":
                r += 1
            
            length = int(s[l:r])
            l = r + 1 + length
            decoded.append(s[r+1:l])
            r = l
        
        return decoded


