class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #find break point
        idx = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i+1] > nums[i]:
                idx = i
                break
        
        if idx == -1:
            self.reverse(nums,0,len(nums)-1)
        else:
            for i in range(len(nums)-1, idx, -1):
                if nums[i] > nums[idx]:
                    self.swap(nums, i, idx)
                    break
            self.reverse(nums, idx+1, len(nums)-1)

    def reverse(self, nums, left , right):
        while(left < right):
            tmp = nums[right]
            nums[right] = nums[left]
            nums[left] = tmp
            left += 1
            right -= 1
    
    def swap(self, nums, start, end):
        tmp = nums[end]
        nums[end] = nums[start]
        nums[start] = tmp

        