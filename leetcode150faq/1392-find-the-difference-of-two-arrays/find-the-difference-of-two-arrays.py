class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        set_num1 = set(nums1)
        set_num2 = set(nums2)
        ans_num1 = set()
        ans_num2 = set()

        for num1 in nums1:
            if num1 not in set_num2:
                ans_num1.add(num1)
        for num2 in nums2:
            if num2 not in set_num1:
                ans_num2.add(num2)
        
        return [list(ans_num1),list(ans_num2)]
        


