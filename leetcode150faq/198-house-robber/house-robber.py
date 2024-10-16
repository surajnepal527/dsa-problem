class Solution:
    def rob(self, nums: List[int]) -> int:
        k = len(nums)
        memo = [-1] * (k+1)
        def solve(house):
            if house >= k: return 0
            if memo[house] != -1: return memo[house]
            #keep
            suma = nums[house] + solve(house+2)
            #skip
            sumb = solve(house+1)
            memo[house] =  max(suma, sumb)
            return memo[house]
        return solve(0)
