class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set()
        for num in nums:
            numbers.add(num)
        
        streak = 0
        for num in numbers:
            n = num
            tempStreak = 1
            while n - 1 in numbers:
                tempStreak += 1
                n -= 1
            
            streak = max(streak, tempStreak)
        
        return streak
