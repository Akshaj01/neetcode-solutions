class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxcount = 0
        for num in nums:
            if (num - 1) not in seen:
                cnt = 1
                while (num + cnt) in seen:
                    cnt += 1
                maxcount = max(maxcount, cnt)
        return maxcount
    
        