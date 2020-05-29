class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) ==0:
            return 0
        map = {}
        start = 0
        max_len = 0
        
        for i in range(len(s)):
            if s[i] in map and map[s[i]] >= start:
                start = map[s[i]]+1
                
            else:
                max_len = max(max_len,i-start+1)
            map[s[i]] = i
            
        return max_len
