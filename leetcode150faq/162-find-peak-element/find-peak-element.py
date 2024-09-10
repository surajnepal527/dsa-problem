class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        n = len(nums)
        #check left edge:
        if nums[0] > nums[1]:
            return 0
        if nums[n-1] > nums[n-2]:
            return n-1
        left = 0 
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left)/2
            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid-1] > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
            

