class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_arr = [0]*n
        suffix_arr = [0]*n
        res = [0]*n
        prefix_arr[0] = 1
        suffix_arr[n-1] = 1
        for i in range(1,n):
            prefix_arr[i] = prefix_arr[i-1] * nums[i-1]
        for j in range(n-2, -1,-1):
            suffix_arr[j] = suffix_arr[j+1] * nums[j+1]
        for k in range(n):
            res[k] = prefix_arr[k] * suffix_arr[k]
        return res
