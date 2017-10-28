#Given a roman numeral, convert it to an integer.

#Input is guaranteed to be within the range from 1 to 3999.

class Solution(object):
    def romanToInt(self,str):
        
	    j = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
	    res = 0
	    i = 0
	    while ( i < len(str)):
		    s1 = j[str[i]]
		    if(i+1 < len(str)):
			    s2 = j[str[i+1]]
			    if(s1>=s2):
				    res=res+s1
				    i=i+1
			    else:
				    res=res+s2-s1
				    i=i+2
		    else:
			    res = res + s1
			    i=i+1
	    return res
