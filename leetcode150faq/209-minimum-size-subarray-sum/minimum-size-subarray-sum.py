class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        for m in range(len(nums)):
            if nums[m] >= target:
                return 1
        
        prefix_sum_array = [0]*len(nums)
        prefix_sum_array[0] = nums[0]
        for k in range(1, len(nums)):
            prefix_sum_array[k] = prefix_sum_array[k-1] + nums[k]

        i = 0 
        j = 1 
        cur_count = 0
        min_count = len(nums) + 1
        while i < len(nums) and j < len(nums):
            if (i == 0 and target > prefix_sum_array[j]) or (i > 0  and target > prefix_sum_array[j] - prefix_sum_array[i-1]):
                j+= 1
            elif (i == 0 and target == prefix_sum_array[j]) or (i > 0  and target == prefix_sum_array[j] - prefix_sum_array[i-1]):
                if j-i+1 < min_count:
                    min_count = j-i+1
                i += 1
                j += 1
            else:
                if j-i+1 < min_count:
                    min_count = j - i + 1
                i += 1

        if min_count == len(nums) + 1:
            return 0
        else:
            return min_count
                
