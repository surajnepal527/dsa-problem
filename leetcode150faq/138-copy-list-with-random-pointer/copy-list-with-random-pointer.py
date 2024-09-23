"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        while cur:
            n_node = Node(cur.val)
            next = cur.next
            cur.next = n_node
            n_node.next = next
            cur = next
        
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        #lets extract the new node here now
        cur = head
        copy_head = None
        if head:
            copy_head = head.next
        while cur:
            copy_node = cur.next
            cur.next = copy_node.next
            if copy_node.next:
                copy_node.next = copy_node.next.next
            cur = cur.next
        return copy_head



        