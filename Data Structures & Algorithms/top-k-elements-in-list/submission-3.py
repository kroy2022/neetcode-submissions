class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        nums=[4,1,-1,2,-1,2,3]
        k=2
        {
            4: 1,
            1: 1,
            -1: 2,
            2: 2,
            3: 1
        }
        occ = [1, 2] top = [-1, 4]
        """
        # num : occurences
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 0
            
            dic[n] += 1
        
        # array storing occurences?
        occ = [float("-inf")] * k

        # Find top k occurences
        for key in dic:
            if occ[0] < dic[key]:
                occ[0] = dic[key]
            
            occ.sort()
        
        # Map occurences to values and return arr
        top = []
        for key in dic:
            if dic[key] in occ:
                top.append(key)

        return top

