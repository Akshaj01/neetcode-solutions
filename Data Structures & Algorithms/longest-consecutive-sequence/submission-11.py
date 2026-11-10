class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

        for i in range(len(nums)):
            length = 0
            if (nums[i] - 1) in seen:
                continue
            while (nums[i] + length) in seen:
                length += 1
                longest = max(longest, length)
        
        return longest





        