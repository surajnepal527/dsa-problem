class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low=mid=0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                self.swap(nums,low, mid)
                mid += 1
                low += 1
            elif nums[mid] == 2:
                self.swap(nums, mid, high)
                high -= 1
            else:
                mid += 1
                
    
    def swap(self, nums, start, end):
        tmp = nums[end]
        nums[end] = nums[start]
        nums[start] = tmp
