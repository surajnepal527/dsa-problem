class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_length, cur_max_length = 0, 0
        max_val = max(nums)
        for num in nums:
            if num == max_val:
                cur_max_length += 1
                max_length = max(cur_max_length, max_length)
            else:
                cur_max_length = 0
        return max_length


