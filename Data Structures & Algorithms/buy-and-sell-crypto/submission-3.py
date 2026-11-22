class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        maxP = 0

        while r < len(prices):
            if prices[r] <= prices[l]:
                l = r
            maxP = max(maxP, prices[r] - prices[l])
            r += 1
    
        return maxP
        
            

        