class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxcnt = 0
        for num in nums:
            #if head 
            if (num - 1) not in seen:
                cnt = 1
                while (num + cnt) in seen:
                    cnt += 1
                maxcnt = max(maxcnt, cnt)
        
        return maxcnt
            

            




        