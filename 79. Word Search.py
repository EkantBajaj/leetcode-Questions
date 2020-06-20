class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])
        
        def found(i,j,idx,visited):
            if idx == len(word):
                return True
            if i<0 or i>=R or j<0 or j>=C or (i,j) in visited :
                return False
            if board[i][j]==word[idx]:
                
                return found(i+1,j,idx+1,visited+[(i,j)]) or found(i-1,j,idx+1,visited+[(i,j)]) or found(i,j+1,idx+1,visited+[(i,j)]) or found(i,j-1,idx+1,visited+[(i,j)])
            
            
        for i in range(R):
            for j in range(C):
                
                if board[i][j]==word[0]:
                    if found(i,j,0,[]): return True
                    
        return False
                
        
