class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        lis = [[1]]
        for i in range(numRows-1):
            sublis=[1]
            for j in range(len(lis[-1])-1):
                sublis.append(lis[-1][j]+lis[-1][j+1])
            sublis.append(1)
            lis.append(sublis)
        return lis  
