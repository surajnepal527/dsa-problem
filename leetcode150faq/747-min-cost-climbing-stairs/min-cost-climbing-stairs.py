class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        tmp = [0] * n
        tmp[0] = cost[0]
        tmp[1] = cost[1]
        for i in range(2, n,1):
            tmp[i] = cost[i] + min(tmp[i-1], tmp[i-2])
        
        return min(tmp[n-1], tmp[n-2])
