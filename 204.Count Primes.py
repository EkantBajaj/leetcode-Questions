class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        is_prime = [True for _ in range(n)]
        
        up = round(n**0.5)
        is_prime[0]=False
        is_prime[1]=False
        for i in range(2,up+1):
            if not is_prime[i]:
                continue
            for j in range(i*i,n,i):
                is_prime[j]=False
        return sum(is_prime)
