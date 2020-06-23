class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
    
        intervals.sort(key= lambda x : x[0])
        
        prev_start = -float('inf') 
        
        for start,end in intervals:
            if start < prev_start:
                return False
            prev_start = end
                
        return True
