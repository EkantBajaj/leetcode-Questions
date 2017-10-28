#Given an integer, convert it to a roman numeral.

#Input is guaranteed to be within the range from 1 to 3999.

class Solution(object):
    def intToRoman(self,int):
	    a=[]
	    while(int>=1000):
		int-=1000
		a.append('M')
	    while(int>=900):
		int-=900
		a.append('CM')
	    while(int>=500):
		int-=500
		a.append('D')
	    while(int>=400):
		int-=400
		a.append('CD')
	    while(int>=100):
		int-=100
		a.append('C')
	    while(int>=90):
		int-=90
		a.append('XC')
	    while(int>=50):
		int-=50
		a.append('L')
	    while(int >=40):
		int-=40
		a.append('XL')
	    while(int >= 10):
		int-=10
		a.append('X')
	    if(int >= 9):
		int-=9
		a.append('IX')
	    elif(int>=5):
		int-=5
		a.append('V')
	    elif(int>=4):
		int-=4
		a.append('IV')
	    while(int>=1):
		int-=1
		a.append('I')
	    b=''.join(a)
	    return b
