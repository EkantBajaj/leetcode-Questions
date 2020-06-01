class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        
        for each in strs:
            ans[tuple(sorted(each))].append(each)
            
        return ans.values()
