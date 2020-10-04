class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        c = collections.Counter(nums)
        return sum([c[n-k]>(k==0) for n in c])
