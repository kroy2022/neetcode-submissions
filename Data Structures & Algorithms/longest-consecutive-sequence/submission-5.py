class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # you are at the start of a sequence 
            if num - 1 not in num_set:
                temp_longest = 1
                while num + temp_longest in num_set:
                    temp_longest += 1
                
                longest = max(temp_longest, longest)

        return longest