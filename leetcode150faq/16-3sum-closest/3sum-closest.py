class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort() #nlogn
        n = len(nums)
        closest_sum = float('inf')

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            low, high = i+1, n-1
            while low < high:
                cur_sum = nums[i] + nums[low] + nums[high]
                if abs(cur_sum - target) < abs(closest_sum - target):
                    closest_sum = cur_sum
                if cur_sum == target:
                    return cur_sum
                elif cur_sum < target:
                    low += 1
                else:
                    high -= 1
        return closest_sum