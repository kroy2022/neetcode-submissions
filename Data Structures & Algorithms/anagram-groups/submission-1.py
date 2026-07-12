class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """
        arr = [] * 26 
        askii = ord(strs[1[]])

        strs = ["act","pots","tops","cat","stop","hat"]

        {
            Act: [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
        },
        act 

         

        """

        word = defaultdict(list)
        for i in strs:
            arr = [0] * 26
            for j in i:
                arr[ord(j) - ord('a')] += 1
            word[tuple(arr)].append(i)
        return word.values()
                
        