class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count  = 0,0
        for num in nums:
            if count == 0 or candidate == num:
                count += 1
                candidate = num
            else:
                count -= 1
        return candidate

        