class Solution:
    def climbStairs(self, n: int) -> int:
        if n<2:
            return 1
        i = 2
        dp ={0:1,
            1:1}
        while i <= n:
            dp[i]=dp[i-1]+dp[i-2]
            i+=1
        return dp[n]
        
