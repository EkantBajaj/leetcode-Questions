class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = []
        for char in s:
            if char.isalnum():
                a.append(char.lower())
        b=a.copy()      
        a.reverse()
        print(a)
        print(b)
        
        if b==a:
            return True
        return False
