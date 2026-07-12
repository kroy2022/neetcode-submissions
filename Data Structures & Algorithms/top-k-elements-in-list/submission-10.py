class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = []
        for _ in range(len(nums) + 1):
            counts.append([])
        
        # number, occurences
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 0
            
            dic[num] += 1
        
        for number, occurences in dic.items():
            counts[occurences].append(number)
        
        output = []
        for i in range(len(counts) - 1, -1, -1):
            inner = counts[i]
            for j in range(len(inner)):
                output.append(inner[j])

            if len(output) == k:
                break

        return output