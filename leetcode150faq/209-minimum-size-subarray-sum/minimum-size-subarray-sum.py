class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        min_count = n + 1
        left = 0
        cur_sum = 0
        for right in range(n):
            
            cur_sum += nums[right]
            
            while cur_sum >= target:
                min_count = min(min_count, right - left + 1)
                cur_sum -= nums[left]
                left += 1

        if min_count == n + 1:
            return 0
        else:
            return min_count
            
            
            return min_count if min_count <= n else 0


        