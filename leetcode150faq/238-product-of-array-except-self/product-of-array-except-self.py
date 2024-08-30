class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        prefix = 1
        for i in range(len(nums)):
            if i == 0:
                ans.append(prefix)
            else:
                prefix *= nums[i-1]
                ans.append(prefix)

        suffix = 1
        for j in range(len(nums)-1, -1, -1):
            if j == len(nums) - 1:
                ans[j] = ans[j] * suffix
            else:
                suffix *= nums[j+1]
                ans[j] *= suffix
        
        return ans

        