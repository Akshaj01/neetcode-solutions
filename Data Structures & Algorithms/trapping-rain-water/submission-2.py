class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft = 0
        maxright = 0
        totalwater = 0

        l = 0
        r = len(height) - 1
        while l < r:
            maxleft = max(maxleft, height[l])
            maxright = max(maxright, height[r])
            totalwater += max(0, min(maxleft, maxright) - height[l])
            totalwater += max(0, min(maxleft, maxright) - height[r])
            
            if maxleft <= maxright:
                l += 1
            
            else:
                r -= 1
        
        return totalwater


        