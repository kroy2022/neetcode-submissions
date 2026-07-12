class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for s in strs:
            sorted_s = [0] * 26
            for c in s:
                sorted_s[ord(c) - ord('a')] += 1
            
            sorted_s = tuple(sorted_s)
            if sorted_s not in dic:
                dic[sorted_s] = []

            dic[sorted_s].append(s)
        
        return list(dic.values())