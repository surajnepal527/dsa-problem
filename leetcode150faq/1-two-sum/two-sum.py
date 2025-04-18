class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for index, num in enumerate(nums):
            comp = target - num
            if comp in num_map:
                return [num_map[comp], index]
            if num not in num_map:
                num_map[num] = index
        
        