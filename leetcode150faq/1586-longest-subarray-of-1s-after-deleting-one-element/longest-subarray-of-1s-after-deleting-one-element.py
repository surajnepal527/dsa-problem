class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = zero_count= max_len = 0
        all_ones = True
        for right in range(len(nums)):
            if nums[right] == 0:
                all_ones = False
                zero_count += 1
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            max_len = max(max_len, right - left)
        
        return max_len

        #return max_len if not all_ones else max_len - 1


        