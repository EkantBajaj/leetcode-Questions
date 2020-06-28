class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profit = 0
        mini = prices[0]
        
        for i in range(1,len(prices)):
            if prices[i]<mini:
                mini = prices[i]
            else:
                profit = max(profit,prices[i]-mini)
        
        return profit
        
        
