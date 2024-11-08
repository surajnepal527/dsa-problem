class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for l in range(1, n-1):
            for start in range(1, n-l):
                end = start+l-1
                for k in range(start, end+1):
                    dp[start][end] = max(dp[start][end], dp[start][k-1] + nums[start-1]*nums[k]*nums[end+1] + dp[k+1][end])
        return dp[1][n-2]
        