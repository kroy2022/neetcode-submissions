class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for s in strs:
            sorted_s = ''.join(sorted(s))

            if sorted_s not in dic:
                dic[sorted_s] = []
            
            dic[sorted_s].append(s)
        
        arr = []
        for key in dic:
            arr.append(dic[key])
        
        return arr