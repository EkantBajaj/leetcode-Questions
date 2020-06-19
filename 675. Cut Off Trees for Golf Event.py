class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        
        target = [(val,r,c ) for r,row in enumerate(forest) for c,val in enumerate(row) if val >1]
        target.sort(key=lambda x:x[0])
        
        sr=sc=ans = 0
        
        for _,r,c in target:
            
            d = self.find_shortest_dist(forest,sr,sc,r,c)
            if d<0 : return -1
            
            ans += d
            sr,sc=r,c
        return ans
        
    def find_shortest_dist(self,forest,sr,sc,tr,tc):
        R,C = len(forest),len(forest[0])
        q = collections.deque([(sr,sc,0)])
        visited = {(sr,sc)}
        
        while q:
            r,c,d = q.popleft()
            
            if tr==r and tc==c:
                return d
            for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0<=nr<R  and 0<=nc<C and (nr,nc) not in visited and forest[nr][nc]:
                    q.append((nr,nc,d+1))
                    visited.add((nr,nc))
        return -1
        
        
        
