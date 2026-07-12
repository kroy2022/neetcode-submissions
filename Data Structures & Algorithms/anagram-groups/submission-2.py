class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
               a,b,c,d,e,f
        arr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        {
            [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] : [abc, cba]
        }
        """ 

        dic = defaultdict(list)

        for i in strs:
            arr = [0] * 26
            for char in i:
                arr[ord(char) - ord('a')] += 1
            dic[tuple(arr)].append(i)
        return list(dic.values())

