class Solution:
    def reverseBits(self, n: int) -> int:
         return int('0b' + (str(bin(n))[2:]).zfill(32)[::-1], 0)
        
