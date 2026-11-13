class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)

        prefix = [0] * length
        prefix[0] = 1

        suffix = [0] * length
        suffix[-1] = 1

        for i in range(1, length):
            prefix[i] = nums[i-1] * prefix[i - 1]
        
        for i in range(length - 2, -1, -1):
            suffix[i] = nums[i+1] * suffix[i+1]
        
        res = [0] * length
        for i in range(length):
            res[i] = prefix[i] * suffix[i]
        
        return res

        




