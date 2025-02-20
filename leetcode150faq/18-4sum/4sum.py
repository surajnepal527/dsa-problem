class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                lo , hi = j+1 , n-1
                while lo < hi:
                    cur_sum = nums[i] + nums[j] + nums[lo] + nums[hi]
                    if cur_sum == target:
                        res.append([nums[i], nums[j], nums[lo], nums[hi]])
                        lo += 1
                        hi -= 1
                        while lo < hi and nums[lo] == nums[lo - 1]:
                            lo += 1
                        while lo < hi and nums[hi] == nums[hi  +1]:
                            hi -= 1
                    elif cur_sum < target:
                        lo += 1
                    else:
                        hi -= 1
        return res
                    
        