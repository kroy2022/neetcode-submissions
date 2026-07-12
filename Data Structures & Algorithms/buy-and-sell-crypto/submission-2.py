class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0 
        r = 1
        for r in range(len(prices)):
            tempProfit = 0
            if prices[l] >= prices[r]:
                l = r
            else:
                tempProfit = prices[r] - prices[l]
            
            profit = max(profit, tempProfit)

        return profit

