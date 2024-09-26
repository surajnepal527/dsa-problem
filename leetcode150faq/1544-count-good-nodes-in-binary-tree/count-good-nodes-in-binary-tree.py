# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = [0]
        max_so_far = root.val
        def dfs(root,max_so_far):
            if not root: return
            if root.val >= max_so_far: 
                max_so_far = root.val
                count[0] += 1
            dfs(root.left, max_so_far)
            dfs(root.right, max_so_far)
        dfs(root, max_so_far)
        return count[0]

                
            
        