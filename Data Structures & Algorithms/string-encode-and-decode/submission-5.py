class Solution:

    def encode(self, strs: List[str]) -> str:

        one_word = ''
        sym = '#'

        """
        ex..
        ["neet","code","love","you"]
            |
        """
        for i in strs:
            word_length = str(len(i))
            one_word += f'{word_length}{sym}{i}'
        return one_word

            


    def decode(self, s: str) -> List[str]:
        
        """
        ex..
        s = "4#neet4#code4#love3#you"
    p1:      |
    p2:       |
        """
        strs = []
        p1 = 0 
         

        while (p1 < len(s)):
            p2 = p1
            while(s[p2] != '#'):
                p2 += 1
            length = int(s[p1:p2])
            p1 = p2 + 1
            p2 = p1 + length
            strs.append(s[p1:p2])
            p1 = p2

        return strs



                



