class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        for c in s:
            hashmap[c]=hashmap.get(c,0)+1
            
        for i,c in enumerate(s):
            if hashmap[c]==1:
                return i
        return -1
