class Solution:
    def countAndSay(self, n: int) -> str:
        def countIt(num):
            ret=''
            left=0
            right=0
            while right<len(num):
                if num[left]==num[right]:
                    right+=1
                else:
                    ret=ret+str((right-left))+num[left]
                    left=right
            else:
                ret=ret+str((right-left))+num[left]
            return ret          
        
        if n==0:return ''
        if n==1:return '1'
        if n<0:return 
        num='1'
        for i in range(1,n):
            num=countIt(num)
        return num
