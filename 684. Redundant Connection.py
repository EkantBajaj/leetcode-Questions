class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = []
        
        def find(x):
            return x if parent[x]==x else find(parent[x])
        
        n = len(edges)
        
        for i in range(n+1):
            parent.append(i)
            
        res = [2,0]
        
        for i in range(n):
            x = find(edges[i][0])
            y = find(edges[i][1])
            if x !=y:
                parent[y]=x
            else:
                res[0]=edges[i][0]
                res[1]=edges[i][1]
                
        return res
