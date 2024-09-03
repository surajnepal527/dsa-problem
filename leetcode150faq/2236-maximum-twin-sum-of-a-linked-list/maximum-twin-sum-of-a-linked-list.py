import sys
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        old_to_new = {}
        current = head
        while current:
            old_to_new[current] = ListNode(current.val)
            current = current.next
    
        current = head
        while current:
            if current.next:
                old_to_new[current].next = old_to_new[current.next]
            current = current.next

        new_current = old_to_new[head]
        prev = None
        while new_current:
            next = new_current.next
            new_current.next = prev
            prev = new_current
            new_current = next
        
        new_head = prev
        max_sum = 0
        cur_sum = 0
        while head and new_head:
            cur_sum = head.val + new_head.val
            max_sum = max(max_sum, cur_sum)
            head = head.next
            new_head = new_head.next
        
        return max_sum




    
        