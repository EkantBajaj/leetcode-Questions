class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        h = len(height)-1
        max_area = 0
        
        while (l<h):
            max_area = max(max_area,min(height[l],height[h])*(h-l))
            if height[l]>height[h]:
                h-=1
            else :
                l+=1
        return max_area
