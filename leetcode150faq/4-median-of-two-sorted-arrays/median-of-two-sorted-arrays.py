class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3, i , j, k = [0]*(len(nums1) + len(nums2)),0,0,0
        while i < len(nums1) and j <len(nums2):
            if nums1[i] < nums2[j]:
                nums3[k] = nums1[i]
                i += 1
            else:
                nums3[k] = nums2[j]
                j += 1
            k += 1
        while i < len(nums1):
            nums3[k] = nums1[i]
            i+= 1
            k += 1
        while j < len(nums2):
            nums3[k] = nums2[j]
            j += 1
            k += 1
        
        if len(nums3)%2==0:
            n = len(nums3)//2
            val1 , val2= nums3[n], nums3[n-1]
            return (val1+val2)/2
        else:
            return nums3[(len(nums3)-1)//2]
        