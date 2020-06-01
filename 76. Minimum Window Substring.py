class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        dict_t = Counter(t)
        
        window_count = collections.defaultdict(int)
        
        req = len(dict_t)
        formed = 0
        ans = float('inf'),None,None
        r,l=0,0
        
        while r<len(s):
            char = s[r]
            window_count[char]+=1
            
            
            
            if char in dict_t and window_count[char]==dict_t[char]:
                formed +=1
            
            while l<=r and formed==req:
                char = s[l]
                
                if r-l+1 < ans[0]:
                    ans = (r-l+1,l,r)
                    
                window_count[char]-=1
                
                if char in dict_t and window_count[char]<dict_t[char]:
                    formed-=1
                l+=1
            r+=1
         
        return "" if ans[0]==float('inf') else s[ans[1]:ans[2]+1]
        
