class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int] )-> float:
        if len(nums1) > len(nums2): #nums1 must be smaller list
            nums1, nums2 = nums2, nums1

        l = 0
        r = len(nums1) #r is count of left of slice
        totallen = len(nums1) + len(nums2)

        while l <= r:
            #get midpt
            amidpt = (l + r) // 2
            bmidpt = (totallen) // 2 - amidpt
            #left half of A
            #left half of b
            A_left = nums1[amidpt - 1] if amidpt > 0 else float("-inf")
            A_right = nums1[amidpt] if amidpt < len(nums1) else float("inf")
            B_left = nums2[bmidpt - 1] if bmidpt > 0 else float("-inf")
            B_right = nums2[bmidpt] if bmidpt < len(nums2) else float("inf")

            bigleft = max(A_left, B_left)
            smallright = min(A_right, B_right)

            #if smallest of right half is greater than biggest of left half valid
            if bigleft <= smallright:
                if totallen % 2 == 0:
                    return (bigleft + smallright) / 2
                else:
                    return smallright
            #else adjust like a dhoat
            elif A_left > B_right:
                r = amidpt - 1
            else:
                l = amidpt + 1


                

            




        