class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minbananarate = 10000000000
        totalbananas = 0
        for i in piles:
            totalbananas = totalbananas + i

        l = 1
        r = totalbananas

        #binary search over banana/h
        while l <= r:
            midrate = (l + r) // 2
            currhours = 0
            for pile in piles:
                currhours += math.ceil(pile / midrate)
            if currhours <= h:
                minbananarate = min(minbananarate, midrate)
                r = midrate - 1
            else:
                l = midrate + 1
            
        
        return minbananarate
            

            

        