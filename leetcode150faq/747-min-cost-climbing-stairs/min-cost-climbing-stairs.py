class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        t = [-1] * (len(cost) + 1)
        return min (self.solve(0, cost, t) , self.solve(1, cost, t))

    def solve(self, idx, cost, t):
        if idx >= len(cost):
            return 0
        if t[idx] != -1:
            return t[idx]
        a = cost[idx] + self.solve(idx + 1, cost,t)
        b = cost[idx] + self.solve(idx+2, cost,t)
        t[idx] =  min(a, b)
        return t[idx]
        