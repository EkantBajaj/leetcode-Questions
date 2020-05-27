class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def permuteHelper(nums,arr,answers):
            if len(nums)==0:
                answers.append(list(arr)
            for i in range(len(nums)):
                elem = nums[i]
                arr.append(elem)
                permuteHelper(nums[:i]+nums[i+1:],arr,answers)
                arr.pop()
                
        arr = list()
        answers = list()
        
        permuteHelper(nums,arr,answers)
        
        return answers
