class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [0]+[amount+1]*amount
        
        for value in range(amount+1):
          
            for coin in coins:
                if coin <= value:
                    dp[value]= min(dp[value],1+dp[value-coin])
    
        return -1 if dp[amount]>amount else dp[amount]
        
