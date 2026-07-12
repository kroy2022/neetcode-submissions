class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}#{s}")

        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        """
        s = 4#neet4#code4#love10#youtututut
        """
        decoded = []
        p1 = 0

        while p1 < len(s):
            p2 = p1
            while s[p2] != "#":
                p2 += 1

            length = int(s[p1:p2])
            p1 = p2+1+length
            decoded.append(s[p2+1:p1])        
        
        return decoded