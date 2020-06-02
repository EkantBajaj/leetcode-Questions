class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0]*len(nums)
        
        answer[0]=1
        for i in range(1,len(nums)):
            answer[i] = answer[i-1]*nums[i-1]
            
        r = 1
        for i in range(len(nums)-1,-1,-1):
            answer[i] = answer[i]*r
            r *= nums[i]
            
        return answer
