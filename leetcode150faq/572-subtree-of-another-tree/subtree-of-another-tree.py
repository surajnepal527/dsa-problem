# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        r1, r2 = root, subRoot
        if not r2:
            return True
        if not r1:
            return False
        if self.isSameTree(r1, r2):
            return True
        return self.isSubtree(r1.left, r2) or self.isSubtree(r1.right, r2)
    

    def isSameTree(self,r1:Optional[TreeNode], r2:Optional[TreeNode]) -> bool:
        if not r1 and not r2: return True
        elif not r1 and r2:return False
        elif r1 and not r2: return False
        elif r1.val != r2.val:return False
        return self.isSameTree(r1.left, r2.left) and self.isSameTree(r1.right, r2.right)

        