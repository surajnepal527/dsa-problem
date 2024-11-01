class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #Lets start with approach one ie. recursion, where we have 2 choice take and not take
        if sum(nums)%2: return False
        totalSum = sum(nums)//2
        memo = [[-1 for _ in range(200)] for _ in range(totalSum+1)]
        def solve(idx, target):
            if target == 0: return True
            if memo[target][idx] != -1: return memo[target][idx]
            if idx == 0: return nums[0] == target
            not_take = solve(idx-1, target)
            take = 0
            if target >= nums[idx]:
                take = solve(idx-1, target-nums[idx])
            memo[target][idx] = take or not_take
            return memo[target][idx]

        return solve(len(nums)-1, totalSum)

        