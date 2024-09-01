class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = -1 
        for i in range(len(nums)):
            if nums[i] != 0:
                if left != -1:
                    nums[i],nums[left] = nums[left],nums[i]
                    left += 1 
            elif left == -1:
                left = i
        


        