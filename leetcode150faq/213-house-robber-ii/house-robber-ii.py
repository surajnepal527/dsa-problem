class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def solve(tmp):
            k = len(tmp)
            if k == 1:
                return tmp[0]
            first, sec, third = 0, tmp[0], 0
            for i in range(2,k+1):
                third = max(tmp[i-1] + first, sec)
                first = sec
                sec = third
            return third
        
        res1 = solve(nums[1:])
        res2 = solve(nums[:-1])
        return max(res1, res2)

        