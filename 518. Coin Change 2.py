class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        sol = [0]*(amount+1)
        sol[0]=1
        for coin in coins:
            for i in range(coin,len(sol)):
                sol[i]+=sol[i-coin]
        return sol[-1]
