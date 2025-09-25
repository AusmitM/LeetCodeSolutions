class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r = 0
        l=0
        maxprof = 0
        while l<len(prices) and r<len(prices):
            prof = prices[r]-prices[l]
            maxprof = max(maxprof, prof)
            if prof<0:
                l=r
            else:
                r+=1
        return maxprof