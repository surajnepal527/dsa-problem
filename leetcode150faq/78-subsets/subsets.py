class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        ans = []
        start = 0
        def solve(start,ans):
            res.append(ans.copy())
            for i in range(start, len(nums)):
                #pick it
                ans.append(nums[i])
                solve(i+1, ans)
                ans.pop()

        solve(start, ans)
        return res       
        