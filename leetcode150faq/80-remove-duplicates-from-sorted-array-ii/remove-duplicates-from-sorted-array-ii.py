class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cc = 1
        i = 0
        for idx, num in enumerate(nums):
            if nums[i] == num and idx != i and cc < 2:
                nums[i+1] = num
                cc += 1
                i += 1
            elif nums[i] != num:
                nums[i+1] = num
                i += 1
                cc = 1
        return i+1
        