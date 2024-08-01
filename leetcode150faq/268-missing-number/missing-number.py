class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_sum = (n  * (n + 1)) / 2
        for i in range (n):
            total_sum -= nums[i]
        
        return total_sum

        