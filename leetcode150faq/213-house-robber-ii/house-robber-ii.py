class Solution:
    def rob(self, nums: List[int]) -> int:
        k = len(nums)
        if k == 1: return nums[0]
        memo = [-1] *(k+1)
        def solve(house, n):
            if house >= n : return 0
            if memo[house] != -1 : return memo[house]
            suma = nums[house] + solve(house+2,n)
            sumb = solve(house+1, n)
            memo[house] =  max(suma, sumb)
            return memo[house]
        a = solve(0, k-1)
        memo = [-1] *(k+1)
        b = solve(1, k)
        return max(a, b)
        