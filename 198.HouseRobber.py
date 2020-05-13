class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        ine = nums[0]
        out = 0
        for i in range(1,len(nums)):
            tmp = ine
            ine = max(ine,out+nums[i])
            out = tmp
        return max(ine,out)
