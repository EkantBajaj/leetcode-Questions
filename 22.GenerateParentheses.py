class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def generateParanthesisHelper(n,string,left,right,arr):
            if len(string)==n*2:
                arr.append(string)
            if (left<n):
                generateParanthesisHelper(n,string+'(',left+1,right,arr)
            if (left>right):
                generateParanthesisHelper(n,string+')',left,right+1,arr)
                
        arr = list()
        generateParanthesisHelper(n,"",0,0,arr)
        
        return arr
