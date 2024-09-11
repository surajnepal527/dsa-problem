class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        t = [-1] * (len(nums) + 1)
        return self.solve(0, nums, t)
    
    def solve(self, idx, nums, t):
        if idx >= len(nums):
            return 0
        if t[idx] != -1:
            return t[idx]

        sum_a = nums[idx] +  self.solve(idx+2, nums , t)
        sum_b = self.solve(idx+1, nums, t)
        t[idx] =  max(sum_a, sum_b)
        return t[idx]
