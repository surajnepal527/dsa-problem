# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        #lets try this with slow fast pointer method
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        cur_n = slow.next
        slow.next = None
        
        while cur_n:
            next = cur_n.next
            cur_n.next = prev
            prev = cur_n
            cur_n = next

        head_n = prev
        head_m = head
        while head_n and head_m:
            m_next = head_m.next
            n_next = head_n.next
            head_m.next = head_n
            head_n.next = m_next
            head_m = m_next
            head_n = n_next




