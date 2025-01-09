class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j, l1, l2, k = 0,0, len(nums1), len(nums2), 0
        mididx = (l1+l2)//2
        el1, el2 = 0, 0
        even = (l1+l2)%2==0
        idx1 = mididx -1
        idx2 = mididx
   
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                if k == idx1:
                    el1 = nums1[i]
                if k == idx2:
                    el2 = nums1[i]
                i += 1
            else:
                if k == idx1:
                    el1 = nums2[j]
                if k == idx2:
                    el2 = nums2[j]
                j += 1
            k += 1

        while i < len(nums1):
            if k == idx1:
                el1 = nums1[i]
            if k == idx2:
                el2 = nums1[i]
            i += 1
            k += 1
        while j < len(nums2):
            if k == idx1:
                el1 = nums2[j]
            if k == idx2:
                el2 = nums2[j]
            j += 1
            k += 1
        if not even:
            return el2/1
        else:
            return (el1+el2)/2




                    

            
                

        