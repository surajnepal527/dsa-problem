class Solution:
    def rob(self, nums: List[int]) -> int:
        k = len(nums)
        if k == 1: return nums[0]
        first, second, third = 0, nums[0], 0
        for i in range(2, k+1):
            third = max(nums[i-1] + first, second)
            first = second
            second = third
        return third
        