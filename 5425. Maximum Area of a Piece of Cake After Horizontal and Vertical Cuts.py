class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        
        max_h=horizontalCuts[0]
        max_v=verticalCuts[0]
        
        for i in range(len(horizontalCuts)-1):
            max_h = max(max_h,horizontalCuts[i+1]-horizontalCuts[i])
        
        max_h = max(max_h,h-horizontalCuts[-1])
        
        for i in range(len(verticalCuts)-1):
            max_v = max(max_v,verticalCuts[i+1]-verticalCuts[i])
        max_v = max(max_v,w-verticalCuts[-1])
        
        return (max_h*max_v)%(10**9 + 7)
