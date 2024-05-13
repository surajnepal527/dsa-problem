class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        output_nums = [0] * n
        if k % n == 0:
            return
        k = k % n
        self.reverse(nums, 0, n -1)
        self.reverse (nums, 0 , k -1)
        self.reverse (nums, k , n -1) 

    def reverse(self, nums, start, end):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start = start + 1
            end = end - 1
        return