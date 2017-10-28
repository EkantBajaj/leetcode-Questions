#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

def match(a,b):
    if(a=='[' and b==']'):
        return 1
    elif(a=='{' and b =='}'):
        return 1
    elif(a=='(' and b==')'):
        return 1
    else:
        return 0
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=[]
        
        for i in range(0,len(s)):
            if(s[i]=='[' or s[i]=='{' or s[i]=='('):
                l.append(s[i])
            elif s[i]==']' or s[i]==')'or s[i]=='}':
                if(len(l)==0):
                    return False
                elif(match(l[len(l)-1],s[i])):
                    del l[-1]
                else:
                    return False
            
        if(len(l)):
            return False
        else:
            return True
