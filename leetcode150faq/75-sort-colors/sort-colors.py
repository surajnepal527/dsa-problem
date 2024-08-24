class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        my_map = {
            0:0,
            1:0,
            2:0
        }
        for i in range(len(nums)):
            my_map[nums[i]] += 1
        k = 0
        count_zero = my_map[0]
        for i in range(count_zero):
            nums[k] = 0
            k += 1
        count_one = my_map[1]
        for i in range(count_one):
            nums[k] = 1
            k += 1
        count_two = my_map[2]
        for i in range(count_two):
            nums[k] = 2
            k += 1
        

            


        