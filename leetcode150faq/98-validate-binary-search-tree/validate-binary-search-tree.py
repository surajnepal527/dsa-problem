# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        high, low = float("infinity"), float("-infinity")
        def dfs(root, high, low):
            if not root:return True
            if not(root.val < high and root.val > low): return False
            left = dfs(root.left, root.val , low)
            right = dfs(root.right, high, root.val)
            return left and right
        return dfs(root, high, low)


        