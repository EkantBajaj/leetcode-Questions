from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = defaultdict(set)
        outdegree = defaultdict(set)
        
        for x,y in prerequisites:
            outdegree[y].add(x)
            indegree[x].add(y)
            
        connections_rem = 0
        indegree_zero = []
        
        for i in range(numCourses):
            if not indegree[i]:
                indegree_zero.append(i)
                connections_rem +=1
        while indegree_zero:
            node = indegree_zero.pop()
                
            for x in outdegree[node]:
                indegree[x].remove(node)
                if not indegree[x]:
                    indegree_zero.append(x)
                    connections_rem +=1
        return connections_rem == numCourses
