import sys
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        result = [-sys.maxsize]
        self.solve(root, result)
        return result[0]
        

    
    def solve(self, root:Optional[TreeNode], result) -> int:
        if not root:
            return 0
        left = self.solve(root.left, result)
        right = self.solve(root.right, result)
        result[0] = max(result[0] , left+right)
        return max(left, right) + 1
