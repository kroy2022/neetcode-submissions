class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Optimal Approach: 
        dic = {value: occurences}
        occ = [[values with occurences at this index]]

        iterate backwards over occ keeping a new array until it is of size k
        """
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 0
            
            dic[n] += 1
        
        occ = []
        for i in range(len(nums)+1):
            occ.append([])
        
        for key in dic:
            occ[dic[key]].append(key)
        
        top = []
        for i in range(len(occ)-1, 0, -1):
            for j in range(len(occ[i])):
                if len(top) == k:
                    return top
                
                top.append(occ[i][j])
        
        return top



