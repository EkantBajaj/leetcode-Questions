class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for i in range(len(s)+1) ]
        
        for i in range(1,len(s)+1):
            if s[0:i] in wordDict:
                dp[i]=True
            else:
                for j in range(i-1,-1,-1):
                    if dp[j] and s[j:i] in wordDict:
                        dp[i]=True
                        
        return dp[len(s)]
