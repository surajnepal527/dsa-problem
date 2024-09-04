# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        res1 = []
        res2 = []
        self.collectLeafNode(res1, root1)
        self.collectLeafNode(res2, root2)
        return res1 == res2

  
        

    def collectLeafNode(self, res, root):
        if not root:
            return
        if not root.left and not root.right:
            res.append(root.val)
        self.collectLeafNode(res, root.left)
        self.collectLeafNode(res, root.right)

        