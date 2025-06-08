# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        max_depth = 1
        queue = deque([(root,1)])
        while queue:
            node, step = queue.popleft()
            if node.left:
                max_depth = max(max_depth, step+1)
                queue.append((node.left, step+1))
            if node.right:
                max_depth = max(max_depth, step+1)
                queue.append((node.right, step+1))
        return max_depth
        

        