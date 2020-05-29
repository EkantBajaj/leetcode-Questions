class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if not str:
            return 0
        
        a = []
        
        if str[0]=='-' or str[0].isnumeric() or str[0]=='+':
            a.append(str[0])
        else:
            return 0
        for i in range(1,len(str)):
            if(not str[i].isnumeric()):
                break
            else:
                a.append(str[i])
        
        if len(a)==1 and not a[0].isnumeric():
            return 0
            
        result = int("".join(a))
        if result > 2**31-1:
            return 2**31-1
        if result < -2**31:
            return -2**31
        return result
        
