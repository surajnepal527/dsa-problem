import sys
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = [-sys.maxsize]
        cur_sum = 0
        def dfs(root, cur_sum):
            if not root:return 0
            left = dfs(root.left, cur_sum)
            right = dfs(root.right, cur_sum)
            cur_sum = left+right+root.val
            max_sum[0] = max(max_sum[0], cur_sum, max(left, right) + root.val, root.val)
            if left <= 0 and right <= 0:
                return root.val
            return max(left, right) + root.val 


        dfs(root, 0)
        return max_sum[0]
        
        