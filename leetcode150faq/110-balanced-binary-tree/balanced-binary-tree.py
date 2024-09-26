# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isHeightBalanced = [True]
       
        def checkHeight(root):
            if root is None:
                return 0
            left = checkHeight(root.left)
            right = checkHeight(root.right)
            diff = abs(left-right)
            if diff > 1:
                isHeightBalanced[0]= False
            return 1 + max(left, right)
        
        checkHeight(root)
        return isHeightBalanced[0]
        