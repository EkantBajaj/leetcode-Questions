class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i,value in enumerate(nums):
            if value in dic:
                return [dic[value],i]
            else:
                dic[target-value]=i
   
