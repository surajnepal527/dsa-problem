class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [0]*len(nums)
        prefix = 1
        postfix = 1
        output[0] = 1
        for i in range(1, len(nums), 1):
            output[i] = prefix * nums[i - 1]
            prefix = output[i]
           
        
        for j in range(len(nums)-1, -1, -1):
            output[j]  *= postfix
            postfix *= nums[j]
        
        return output
            
