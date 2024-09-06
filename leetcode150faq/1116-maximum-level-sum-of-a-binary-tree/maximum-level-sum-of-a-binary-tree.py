from collections import deque 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        max_sum = root.val 
        q = deque([root])
        cur_level = 0
        min_level = 0
        while q:
            qLen = len(q)
            cur_sum = 0
            cur_level += 1
            for i in range(qLen):
                node = q.popleft()
                if node:
                    cur_sum += node.val
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                        
            if cur_sum > max_sum:
                max_sum = cur_sum
                min_level = cur_level
        
        return min_level if min_level > 0 else 1








        