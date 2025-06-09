class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj1, cnt1 = None, 0
        for num in nums:
            if num == maj1:
                cnt1 += 1
            elif cnt1 == 0:
                maj1 = num
                cnt1 += 1
            else:
                cnt1 -= 1
        return maj1
        