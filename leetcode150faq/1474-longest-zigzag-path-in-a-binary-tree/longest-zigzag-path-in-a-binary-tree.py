# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Pair(object):
    def __init__(self, maxLen = 0, forwardSlop = -1, backwardSlop = -1):
        self.maxLen = maxLen
        self.forwardSlop = forwardSlop
        self.backwardSlop = backwardSlop

class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = self.longestZigZag_(root)
        return ans.maxLen
    
    def longestZigZag_(self, root):
        if not root:
            return Pair()
        
        left = self.longestZigZag_(root.left)
        right = self.longestZigZag_(root.right)

        ans = Pair()
        ans.maxLen = max(max(left.maxLen, right.maxLen), max(left.backwardSlop, right.forwardSlop)+1)
        ans.forwardSlop = left.backwardSlop + 1
        ans.backwardSlop = right.forwardSlop + 1
        return ans
        