class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        t = [1] * (n)
        max_lis = 1
        for i in range(n):
            for j in range(i):
                if nums[j]< nums[i]:
                    t[i] = max(t[i], t[j] + 1)
                    max_lis = max(max_lis, t[i])
        return max_lis


        