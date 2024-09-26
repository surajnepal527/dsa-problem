from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        que = deque()
        que.append(root)
        ans = []
        tmp = []
        while que:
            n = len(que)
            tmp = []
            for i in range(n):
                cur_node = que.popleft()
                tmp.append(cur_node.val)
                if cur_node.left:
                    que.append(cur_node.left)
                if cur_node.right:
                    que.append(cur_node.right)
            ans.append(tmp)
        return ans

        
        