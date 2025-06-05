class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1
        left, right = 0, 1
        while right < len(nums):
            if nums[left] == nums[right]:
                right += 1
            else:
                nums[left+1] = nums[right]
                left += 1
                right += 1
        return left + 1
        