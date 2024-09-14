class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        memo = {}
        start = 1
        cur_sum = 0
        mod = 1000000007
        return self.solve(n, x, start, cur_sum , mod, memo)
    
    def solve(self, n , x, cur, cur_sum, mod, memo):
        key = (cur, cur_sum)
        if n == cur_sum:
            return 1
        if cur_sum > n:
            return 0
        cur_power = cur ** x
        if cur_power > n:
            return 0
            
        if key in memo:
            return memo[key]

        pick = self.solve(n, x, cur+1, cur_sum+cur_power, mod,memo)
        skip = self.solve(n, x, cur+1, cur_sum, mod ,memo)

        memo[key] = (pick % mod + skip % mod) % mod
        return memo[key]

        