import sys
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        min_val = sys.maxsize
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            min_val = min(min_val, nums[mid])
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return min_val
            