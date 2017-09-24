#Implement atoi to convert a string to an integer.

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        neg=0
        a=[]
        l=[]
        str=str.lstrip()
        for each in str:
            a.append(each)
        if len(a):
            if a[0]=='+':
                
                a.remove('+')
            elif a[0]=='-':
                a.remove('-')
                neg = 1
            for each in a:
                
                if each.isdigit():
                    
                    l.append(each)
            
                else:
                
                    break
            if len(l):
                
                l=''.join(l)
                l=int(l)
                if neg==1:
                    l= -l
                if l>2147483647:
                    l=2147483647
                if l<-2147483648:
                    l=-2147483648
                return l
            else:
                return 0
        
        else:
            return 0
