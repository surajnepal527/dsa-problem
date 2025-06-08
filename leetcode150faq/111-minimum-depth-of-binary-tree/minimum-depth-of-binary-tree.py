# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        queue = deque([(root, 1)])
        while queue:
            node, step = queue.popleft()
            if not node.left and not node.right:
                return step
            if  node.left:
                queue.append((node.left, step+1))
            if  node.right:
                queue.append((node.right, step+1))

        