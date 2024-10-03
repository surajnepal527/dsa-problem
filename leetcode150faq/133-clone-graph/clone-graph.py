"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #idea is to run the dfs to explore more option
        #dfs helps here to get the copies of neighbour if it already exist in map

        oldToNewMap = {}
        def dfs(node):
            if not node:
                return None
            if node in oldToNewMap:
                return oldToNewMap[node]
            copy = Node(node.val)
            oldToNewMap[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node)
        