class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i,a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            left = i + 1
            right = len(nums)-1
            while left < right:
                cur_sum = a + nums[left] + nums[right]
                if cur_sum < 0:
                    left += 1
                elif cur_sum > 0:
                    right -= 1
                else:
                    res.append([a, nums[left],nums[right]])
                    right -= 1
                    while nums[right] == nums[right+1] and left<right:
                        right -= 1
        return res

