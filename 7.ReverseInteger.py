class Solution:
    def reverse(self, x: int) -> int:
        
        neg=0
        if x<0:
            neg = 1
        x=abs(x)
        
        sum=0
        while x>0:
            sum = sum*10 +(x%10)
            x//=10
        x=sum
        if neg == 1:
            x = -sum
        
        if x >= 2**31 or x <= -(2**31):
            return 0
        return x
            
            
