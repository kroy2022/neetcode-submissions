class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Approach:
        - Have a 2d array of size len(nums)
        - Use the indexes in that array as occurences and make the
        element at that index equal to the number.
        - Iterate backwards over that array k times
        """
        # Create 2d array with length of nums
        occ = []
        for i in range(len(nums)+1):
            occ.append([])

        # Initialize dictionary: { num : occurences }
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 0
            
            dic[num] += 1
        

        for key in dic:
            occ[dic[key]].append(key)
        
        print(dic)
        top_k = []
        for i in range(len(occ)-1, -1, -1):
            if len(top_k) == k:
                break 
            for j in range(len(occ[i])):
                top_k.append(occ[i][j])
                if len(top_k) == k:
                    break

        return top_k
