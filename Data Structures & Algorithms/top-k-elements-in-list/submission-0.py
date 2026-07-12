class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        """
        nums = [1,2,2,3,3,3], k = 2
                

                0.  1.  2.  3.  4.  5.  6.
        freq = [[], [1], [2], [3], [], [], []]

        count
        {
            1 : 1
            2 : 2
            3 : 3       
        }
        """
        
        
        
        count = {}

        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        


        

        