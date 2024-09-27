# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inorder_map =  { num:idx for idx, num in enumerate(inorder)}
        pre_idx = 0
        def dfs(start, end):
            nonlocal pre_idx
            if start > end: 
                return None
            in_idx = inorder_map[preorder[pre_idx]]
            root = TreeNode(preorder[pre_idx])
            pre_idx += 1
            root.left = dfs(start, in_idx-1)
            root.right = dfs(in_idx+1, end)
            return root
        return dfs(0, len(inorder)-1)

        