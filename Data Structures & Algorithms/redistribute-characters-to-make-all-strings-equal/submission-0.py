class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        wordCount = {}

        for word in words:
            for c in word:
                if c not in wordCount:
                    wordCount[c] = 0
                
                wordCount[c] += 1
        
        length = len(words)
        for occurence in wordCount.values():
            if occurence % length != 0:
                return False
        
        return True


