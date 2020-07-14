class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if not matrix:
            return matrix
        if len(matrix)==1:
            return matrix[0]
        output = []
        
        count = 0
        row_top=0
        row_bottom = len(matrix)-1
        col_left=0
        col_right=len(matrix[0])-1
        
        while(row_top<=row_bottom and col_left<= col_right):
            
            if count%4==0:
                for col in range(col_left,col_right+1):
                    output.append(matrix[row_top][col])
                row_top +=1
            elif count%4==1:
                for row in range(row_top,row_bottom+1):
                    output.append(matrix[row][col_right])
                col_right-=1
            elif count%4==2:
                for col in range(col_right,col_left-1,-1):
                    output.append(matrix[row_bottom][col])
                row_bottom-=1
            elif count%4==3:
                for row in range(row_bottom,row_top-1,-1):
                    output.append(matrix[row][col_left])
                col_left+=1
            count+=1
                    
        return output
