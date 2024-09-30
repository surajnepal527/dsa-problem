class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        break_pt = -1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > nums[i-1]:
                break_pt = i-1
                break
        if break_pt == -1:
            self.reverse(nums, 0, len(nums)-1)
            return nums
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > nums[break_pt]:
                nums[i], nums[break_pt] = nums[break_pt], nums[i]
                break
        self.reverse(nums, break_pt+1, len(nums)-1)
        return nums
    def reverse(self, nums:List[int], start:int, end:int):
        while start < end:
            tmp = nums[start]
            nums[start] = nums[end]
            nums[end] = tmp
            start += 1
            end -= 1

        