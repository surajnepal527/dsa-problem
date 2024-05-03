class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return len(nums)
        i = 0
        j = 1
        k = len(nums)
        temp = nums[i]
        tempCount = 1
        while j < len(nums):
            if nums[i] != nums[j]:
                temp = nums[j]
                tempCount = 1
                if j - i > 1:
                    i = i + 1
                    self.swap(nums, i , j)
                else:
                    i = i + 1
                j = j + 1
            else:
                if tempCount > 1:
                    nums[j] = '_'
                    j = j + 1
                    k = k - 1
                else:
                    tempCount = tempCount + 1
                    if j - i > 1:
                        i = i + 1
                        self.swap(nums , i , j)
                        j = j + 1
                    else:
                        i = i + 1
                        j = j + 1
        return k

    def swap(self, nums, start , end):
        temp = nums[end]
        nums[end] = nums[start]
        nums[start] = temp
        return
        