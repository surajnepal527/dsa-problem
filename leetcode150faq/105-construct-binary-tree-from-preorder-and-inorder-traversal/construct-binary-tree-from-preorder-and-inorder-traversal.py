# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        start , end = 0, len(inorder)-1
        idx = [0]
        def dfs(preorder, inorder, idx, start, end):
            if start > end: return None
            root_value = preorder[idx[0]]
            root = TreeNode(root_value)
            idx[0] += 1
            in_idx = -1
            for i in range(start, end+1):
                if root_value == inorder[i]:
                    in_idx = i
                    break
            
            root.left = dfs(preorder, inorder, idx, start, in_idx-1)
            root.right = dfs(preorder, inorder, idx, in_idx+1, end)
            return root
        
        return dfs(preorder,inorder, idx, start, end)
