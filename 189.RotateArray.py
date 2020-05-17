class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        while k > len(nums):
            k = k-len(nums)
        while k > 0:
            nums.insert(0,nums.pop())
            k-=1
