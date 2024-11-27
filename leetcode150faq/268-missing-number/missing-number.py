class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for idx, num in enumerate(nums):
            res ^= idx^num
        return res
        