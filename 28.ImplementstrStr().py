class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        res = -1
        m = len(haystack)
        n = len(needle)
        for i in range(m-n+1):
            if haystack[i:i+n] == needle:
                return i
        return res
