#Determine whether an integer is a palindrome. Do this without extra space.
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        neg = 0
        a=x
        b=[]
        x=str(x)
        for each in x:
            b.append(each)
        if '-' in b:
            b.remove('-')
            b.append('-')
            neg=1
        b.reverse()
        
        r=''.join(b)
        r=int(r)
        if a==r and neg==0:
            return True
        else:
            return False
