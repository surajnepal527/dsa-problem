class Solution:
    def rob(self, nums: List[int]) -> int:
        k = len(nums)
        if k == 1: return nums[0]
        t =[0] * (k + 1)
        t[0], t[1] = 0, nums[0]
        for i in range(2, k+1):
            t[i] = max(nums[i-1] + t[i-2], t[i-1])
        return t[k]
        