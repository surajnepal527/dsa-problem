class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1
        i = 0
        j = 1
        k = len(nums)
        temp = nums[i]
        while j < len(nums):
            if temp == nums[j]:
                nums[j] = '_'
                j = j + 1
                k = k - 1
            else:
                temp = nums[j]
                if j - i > 1:
                    i = i + 1
                    nums[i] = temp
                    nums[j] = '_'
                else:
                    i = i + 1
                j = j + 1
        return k
                


