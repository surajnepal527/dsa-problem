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
        prev = None
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        
        head2 = prev.next
        prev.next = None
        cur = head
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        head1 = prev

        max_sum = -1
        while head1 and head2:
            max_sum = max(max_sum, head1.val + head2.val)
            head1 = head1.next
            head2 = head2.next
        
        return max_sum
 

            
            
