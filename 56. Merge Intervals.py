class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if not intervals:
            return intervals
        result = []
        intervals.sort(key= lambda x:x[0])
        for each in intervals:
            if result:
                if  result[-1][0]<=each[0] <= result[-1][1]:
                    pre = result.pop()
                    result.append([min(pre[0],each[0]),max(pre[1],each[1])])
                else:
                    result.append(each)
            else:
                result.append(each)
        return result
