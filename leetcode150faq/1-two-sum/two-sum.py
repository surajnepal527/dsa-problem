class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        numMap[nums[0]] = 0
        for i in range(1, len(nums)):
            if target - nums[i] in numMap:
                return [numMap[target-nums[i]], i]
            numMap[nums[i]] = i
        
        
        