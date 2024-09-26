# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        isSame = [True]
        root1, root2 = p, q
        def dfs(root1, root2):
            if root1 is None and root2 is None:
                return
            elif root1 is None and root2 is not None:
                isSame[0] = False
                return
            elif root1 is not None and root2 is None:
                isSame[0] = False
                return
            elif root1.val != root2.val:
                isSame[0] = False
                return


            dfs(root1.left, root2.left)
            dfs(root1.right, root2.right)

        dfs(root1, root2)
        return isSame[0]
        


        