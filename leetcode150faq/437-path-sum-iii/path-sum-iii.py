# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.total = 0

    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        if not root:
            return 0
        sum_map ={}
        sum_map[0] = 1
        self.findPathSum(root, 0, targetSum, sum_map)
        return self.total

    def findPathSum(self, root, sum, k, map):
        if not root:
            return
        sum += root.val
        diff = sum - k
        if diff in map:
            self.total += map[diff]
        map[sum] = map.get(sum,0) + 1
        self.findPathSum(root.left, sum, k , map)
        self.findPathSum(root.right, sum, k , map)
        map[sum] = map.get(sum, 0) - 1
        return 

        