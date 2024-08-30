import sys
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        f = sys.maxsize
        s = sys.maxsize
        for i in range(len(nums)):
            if nums[i] <= f:
                f = nums[i]
            elif nums[i] <= s:
                s = nums[i]
            else:
                return True
        return False
        