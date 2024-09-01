class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix_arr = [0] * len(nums)
        sufix_arr = [0] * len(nums)
        left = 0
        right = len(nums) - 1
        for i in range(len(nums)):
            if i == 0:
                prefix_arr[i] = 0
            else:
                prefix_arr[i] = prefix_arr[i-1] + nums[i-1]
        
        for j in range(len(nums)-1, -1, -1):
            if j == len(nums) - 1:
                sufix_arr[j] = 0
            else:
                sufix_arr[j] = sufix_arr[j+1] + nums[j+1]
        
        for i in range(len(nums)):
            if prefix_arr[i] == sufix_arr[i]:
                return i
        
        return - 1