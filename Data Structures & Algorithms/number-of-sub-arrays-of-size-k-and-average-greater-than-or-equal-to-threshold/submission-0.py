class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        """
        arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4

        L = 6
        R = 7
        currSum = 13
        subArrayCount = 3
        """
        subArrayCount = 0
        currSum = 0
        L = 0 
        for R in range(len(arr)):
            currSum += arr[R]
            if R - L < k - 1:
                continue
            
            if currSum / k >= threshold:
                subArrayCount += 1
            
            currSum -= arr[L]
            L += 1
        
        return subArrayCount
            
