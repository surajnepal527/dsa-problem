class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        cur_sum = nums[0]
        for i in range(1,len(nums)):
            cur = nums[i]
            cur_sum = max(cur, cur + cur_sum)
            max_sum = max(cur_sum, max_sum)

        return max_sum
        
                


