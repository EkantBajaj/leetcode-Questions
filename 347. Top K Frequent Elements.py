class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicty = {}
        
        for each in nums:
            dicty[each]=dicty.get(each,0)+1
            
        listy = [(key,v) for key,v in dicty.items()]
    
        listy.sort(key= lambda x: x[1] , reverse = True)
        
        return [listy[i][0] for i in range(k)]
