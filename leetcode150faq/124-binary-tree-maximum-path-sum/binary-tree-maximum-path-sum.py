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
        def dfs(root):
            if not root:return 0
            left = dfs(root.left)
            right = dfs(root.right)
            total_path_sum = left+right+root.val
            left_or_right_path_sum = max(left, right) + root.val
            root_sum = root.val
            max_sum[0] = max(max_sum[0], total_path_sum, left_or_right_path_sum, root_sum)
            if left <= 0 and right <= 0:
                return root.val
            return max(left, right) + root.val 
        dfs(root)
        return max_sum[0]
        
        