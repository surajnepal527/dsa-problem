class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for num in nums:
            if nums[i] != num:
                nums[i+1] = num
                i += 1
        return i+1

        