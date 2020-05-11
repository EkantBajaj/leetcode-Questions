class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_curr = nums[0]
        max_global = nums[0]
        for i in range(1,len(nums)):
            max_curr = max(nums[i],max_curr+nums[i])
            max_global = max(max_curr,max_global)
        return max_global
