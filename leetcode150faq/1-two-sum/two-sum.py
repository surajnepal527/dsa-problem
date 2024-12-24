class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {nums[0]:0}
        for i in range(1, len(nums)):
            diff = target-nums[i]
            if diff in numMap:
                return [numMap[diff], i]
            numMap[nums[i]] = i
        
        
        