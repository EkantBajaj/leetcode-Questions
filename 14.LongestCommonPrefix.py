class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort(key=len)
        brk = 0
        res = []
        i=0
        while i < len(strs[0]):
            a = strs[0][i]
            for each in strs:
                if each[i]!=a:
                    brk =1
            if brk==1:
                break
            else: 
                res.append(a)
                i+=1
            
        return "".join(res)
