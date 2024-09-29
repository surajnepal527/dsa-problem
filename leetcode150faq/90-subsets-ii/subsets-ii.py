class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        start = 0
        nums.sort()
        def solve(start, ans):
            if start >= len(nums):
                res.append(ans.copy())
                return
            #keep
            ans.append(nums[start])
            solve(start+1, ans)
            ans.pop()
            next_index = start + 1
            while next_index < len(nums) and nums[next_index] == nums[start]:
                next_index += 1
            solve(next_index, ans)
        solve(start, [])
        return res
            
        