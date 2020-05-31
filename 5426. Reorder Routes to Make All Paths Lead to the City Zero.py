class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        connections.sort(key= lambda x : x[1])
        reach = {0}
        count=0
        for each in connections:
            if each[1] in reach:
                reach.add(each[0])
            else:
                if each[0] in reach:
                    count+=1
                    reach.add(each[1])
        return count
                
