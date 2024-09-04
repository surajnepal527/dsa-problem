import sys
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_value = -sys.maxsize - 1
        return self.countGoodNodes(root, max_value)

    def countGoodNodes(self, root, max_value):
        if not root:
            return 0
        
        count = 1 if root.val >= max_value else 0
        max_value = max(max_value, root.val)

        count += self.countGoodNodes(root.left, max_value)
        count += self.countGoodNodes(root.right, max_value)
        return count



        