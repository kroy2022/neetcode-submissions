class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        nums = [-1,0,1,2,-1,-4]
        nums = [-1,0,1,2,-1,-4]
        -4,-1,-1,0,1,2

        [-4,-1,-1,0,1,2]
                    | |

        sortedNums = nums.sort()
        for i in emumerate(sortedNums:
            p1, p2 = 


        """
        sortedNums = sorted(nums)  # Sort the input list
        ans = []
        
        for index, val in enumerate(sortedNums):
            if val > 0:
                break  # Since sorted, further values will be >0, making sum >0
            
            if index > 0 and val == sortedNums[index - 1]:
                continue  # Skip duplicate values for `val`
            
            p1, p2 = index + 1, len(sortedNums) - 1
            
            while p1 < p2:
                total = val + sortedNums[p1] + sortedNums[p2]
                
                if total == 0:
                    ans.append([val, sortedNums[p1], sortedNums[p2]])
                    
                    # Move p1 and p2 past duplicate values
                    p1 += 1
                    while p1 < p2 and sortedNums[p1] == sortedNums[p1 - 1]:
                        p1 += 1
                    
                    p2 -= 1
                    while p1 < p2 and sortedNums[p2] == sortedNums[p2 + 1]:
                        p2 -= 1

                elif total < 0:
                    p1 += 1  # Need a larger sum
                else:
                    p2 -= 1  # Need a smaller sum
        
        return ans
