class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        length = len(nums)
        for i in range(length):
            for j in range(i+1,length):
                
                left = j+1
                right = length-1
                
                while left<right:
                    sum = nums[i]+nums[j]+nums[left]+nums[right]
                    
                    if sum == target:
                        ans.append(sorted([nums[i],nums[j],nums[left],nums[right]]))
                        
                        prev_left = nums[left]
                        while(left<right and nums[left]==prev_left):
                            left+=1
                        prev_right = nums[right]
                        while(left<right and nums[right]==prev_right):
                            right -=1
                    elif sum < target:
                        left+=1
                    elif sum > target:
                        right-=1
        
        res = []
        [res.append(x) for x in ans if x not in res]
       
        return res
