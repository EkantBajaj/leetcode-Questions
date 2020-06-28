class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sum = 0
        max_sum = -float('inf')
        
        for num in nums:
            sum = max(sum+num,num)
            
            max_sum = max(max_sum,sum)
          
            
        return max_sum
