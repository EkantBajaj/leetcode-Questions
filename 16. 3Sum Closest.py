class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = sys.maxsize
        nums.sort()
        
        for i in range(len(nums)):
            lo = i+1
            hi = len(nums)-1
            while lo < hi:
                sum = nums[i]+nums[lo]+nums[hi]
                if abs(diff) > abs(target - sum):
                    diff = target-sum
                if sum < target:
                    lo +=1
                else:
                    hi -=1
            if diff == 0 :
                break
        return target-diff
        
