class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        #get mid
        while l < r:
            mid = (l + r) // 2 # get midpt
            
            if nums[mid] > nums[r]: # if pivot on right
                l = mid + 1

            else: # if pivot on left
                r = mid

            
        return nums[l]

        