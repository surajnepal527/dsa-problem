class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        k = len(cost)
        first, second , third = cost[0], cost[1], 0
        for i in range(2, k):
            third = cost[i] + min(first, second)
            first = second
            second = third
        return min(first, second)
        

        