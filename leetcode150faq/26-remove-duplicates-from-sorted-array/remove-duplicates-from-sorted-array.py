class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        cur = nums[0]
        for num in nums:
            if cur != num:
                nums[i] = num
                cur = num
                i += 1
        return i

        