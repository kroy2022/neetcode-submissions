class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Find the largest difference in array where j > i
        - Keep a window of a changing size while your profit is positive
        - When profit goes negative move pointer until you are back at 0
        """
        p1 = 0
        maxProfit = 0
        for i in range(len(prices)):
            profit = prices[i] - prices[p1]

            if profit < 0 and p1 != i:
                profit = 0
                p1 = i
            
            maxProfit = max(profit, maxProfit)

        return maxProfit