class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        i = 0
        ans = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, n-1
            while left < right:
                cur_sum = nums[left] + nums[right]+ nums[i]
                if cur_sum > 0:
                    right -= 1
                elif cur_sum < 0:
                    left += 1
                else:
                    ans.append([nums[left], nums[right], nums[i]])
                    left += 1
                    while nums[left] == nums[left -1] and left < right:
                        left += 1
        return ans
                    

                
        