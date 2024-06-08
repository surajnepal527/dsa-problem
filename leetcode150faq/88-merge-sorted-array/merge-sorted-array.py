class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = len(nums1) - 1
        for k in range(len(nums1)-1, -1, -1):
            if i < 0:
                nums1[k] = nums2[j]
                j -= 1
            elif j < 0:
                nums1[k] = nums1[i]
                i -= 1
            elif nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
        