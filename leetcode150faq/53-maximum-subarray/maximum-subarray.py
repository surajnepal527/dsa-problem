class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cs,ms = 0, nums[0]
        for num in nums:
            if cs < 0:
                cs = 0
            cs += num
            ms = max(ms, cs)
        return ms
        