class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        t = [-1] * (n + 1)
        t[0] = 0
        t[1] = nums[0]
        for i in range(2, n+1):
            steal = nums[i-1] + t[i-2]
            skip = t[i-1]
            t[i] = max(steal, skip)
        
        return t[n]

        