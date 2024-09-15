class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prefix - array
        n = len(nums)
        pre_arr = [0]*n
        suf_arr = [0]*n
        pre_arr[0] = 1
        suf_arr[n-1] = 1
        ans = []
        for i in range(1, n):
            pre_arr[i] = pre_arr[i-1] * nums[i-1]
        
        for j in range(n-2, -1, -1):
            suf_arr[j] = suf_arr[j+1] * nums[j+1]
        
        for k in range(len(nums)):
            ans.append(pre_arr[k] * suf_arr[k])

        return ans

        
        