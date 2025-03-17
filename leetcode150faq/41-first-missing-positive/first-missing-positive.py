class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #first let check if 1 is present or not i.e first positive number
        contains1 = False
        for i in range(len(nums)):
            if nums[i] == 1:
                contains1 = True
            elif nums[i] > len(nums) or nums[i] <= 0:
                nums[i] = 1
        
        if not contains1:
            return 1
        
        for i in range(len(nums)):
            num = abs(nums[i])
            idx = num - 1
            if nums[idx] < 0: 
                continue
            else:
                nums[idx] = nums[idx]*-1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return i+1
        
        return len(nums) +1

