class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        i = 0
        nums_map = {}
        while i < len(nums):
            if nums[i] in nums_map:
                newCount = (nums_map.get(nums[i]) + 1)
                if newCount > (len(nums)/2):
                    return nums[i]
                else:
                    nums_map[nums[i]] = newCount
            else:
                nums_map[nums[i]] = 1
            i = i + 1

        