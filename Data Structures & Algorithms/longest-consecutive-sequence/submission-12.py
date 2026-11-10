class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

        for i in seen:
            length = 0
            if (i - 1) in seen:
                continue
            while (i + length) in seen:
                length += 1
                longest = max(longest, length)
        
        return longest





        