import sys
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre=suf=1
        res = -sys.maxsize
        n = len(nums)
        for i in range(n):
            if pre == 0:
                pre = 1
            if suf == 0:
                suf = 1
            pre = pre * nums[i]
            suf = suf * nums[n-i-1]
            res = max(res, max(pre, suf))
        return res

        