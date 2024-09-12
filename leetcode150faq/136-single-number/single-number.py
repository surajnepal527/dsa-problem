class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.solve(nums, 0)
    
    def solve(self, nums, idx):
        if idx == len(nums) -1:
            return nums[idx]
        return nums[idx] ^ self.solve(nums, idx+1)