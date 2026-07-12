class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        nums = [0,3,2,5,4,6,1,1]
        """


        set_num = set(nums)
        longest = 0 
        for i in set_num:
            if (i - 1) not in set_num:
                length = 1
                while(i + length) in set_num:
                    length += 1 
                longest = max(length, longest)
        return longest

