class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        prices = [10,1,5,6,7,1]
        """
        profit = 0
        for i in range(len(prices)):
            tempProfit = 0
            for j in range(i, len(prices)):
                if prices[j] - prices[i] > tempProfit:
                    tempProfit = prices[j] - prices[i]

            profit = max(tempProfit, profit)
        
        return profit
