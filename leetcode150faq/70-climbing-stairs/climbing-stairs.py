class Solution:
    def climbStairs(self, n: int) -> int:
        ways_for_n_stair = [0] * (n+1)
        ways_for_n_stair[0] = 0
        ways_for_n_stair[1] = 1
        if n == 1:
            return ways_for_n_stair[n]
        ways_for_n_stair[2] = 2
        if n == 2:
            return ways_for_n_stair[n]
        for i in range(3, n+1):
            ways_for_n_stair[i] = ways_for_n_stair[i-1] + ways_for_n_stair[i-2]
        return ways_for_n_stair[n]
        