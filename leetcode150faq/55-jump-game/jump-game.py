class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        j = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= j - i:
                j = i
        
        if j == 0:
            return True
        
        return False
