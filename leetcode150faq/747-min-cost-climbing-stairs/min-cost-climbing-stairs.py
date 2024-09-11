class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        # tmp = [0] * n
        # tmp[0] = cost[0]
        # tmp[1] = cost[1]
        for i in range(2, n,1):
            cost[i] = cost[i] + min(cost[i-1], cost[i-2])
        
        return min(cost[n-1], cost[n-2])
