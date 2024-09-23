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
        dummy_p = Node(0)
        n_head = dummy_p
        node_map = {}
        while cur:
            cur_p = Node(cur.val)
            dummy_p.next = cur_p
            node_map[cur] = cur_p
            cur = cur.next
            dummy_p = dummy_p.next

        n_cur = head
        while n_cur:
            p_cur = node_map[n_cur]
            o_ran = n_cur.random
            if o_ran:
                p_ran = node_map[o_ran]
                p_cur.random = p_ran
            n_cur = n_cur.next

        return n_head.next


        