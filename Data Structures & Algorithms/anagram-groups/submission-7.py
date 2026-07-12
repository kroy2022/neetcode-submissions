class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        dic = {
            act = [act]
        }
        sort = opst
        """

        dic = {}

        for s in strs:
            sort = ''.join(sorted(s))

            if sort not in dic:
                dic[sort] = []
            
            dic[sort].append(s)
        
        output = []
        for val in dic.values():
            output.append(val)
        
        return output