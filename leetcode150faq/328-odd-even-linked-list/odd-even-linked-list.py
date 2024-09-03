# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #handle edge case where head in null or head .next is none
        if head is None or head.next is None:
            return head
        
        odd = head
        even = head.next
        even_head = head.next

        while even and even.next:
            #odd.next = even.next
            odd.next = odd.next.next
            odd = odd.next

            #even.next = odd.next
            even.next = even.next.next
            even = even.next
        
        odd.next = even_head
        return head