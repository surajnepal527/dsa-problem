class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        i = 0
        total = 0
        while i < k:
            total += nums[i]
            i += 1
        max_avg = float(total) / float(k)
        left = 0
        right = i
        cur_total = total
        while right < len(nums):
            cur_total = cur_total - nums[left] + nums[right]
            max_avg = max(float(max_avg), float(cur_total)/float(k) )
            right += 1
            left += 1
        
        return max_avg


        