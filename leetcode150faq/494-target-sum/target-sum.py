class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def solve(idx, cur_sum):
            if idx == len(nums) and cur_sum == target: return 1
            if idx == len(nums) and cur_sum != target: return 0
            if (idx, cur_sum) in memo: return memo[(idx, cur_sum)]
            memo[(idx, cur_sum)] = solve(idx+1, cur_sum-nums[idx]) + solve(idx+1, cur_sum+nums[idx])
            return memo[(idx, cur_sum)]
        return solve(0,0)

        