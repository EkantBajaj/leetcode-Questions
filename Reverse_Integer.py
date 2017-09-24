#Reverse digits of an integer.

#Example1: x = 123, return 321
#Example2: x = -123, return -321

#The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = []
        x = str(x)
        for each in x:
            l.append(each)
        
        if '-' in l:
            l.remove('-')
            l.append('-')
        l.reverse()
        num = ''.join(map(str,l))
        num = int(num)
        if (abs(num) >> 31):
            return 0
        else:
            return num
