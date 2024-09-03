# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #solution 2 : using fast slow two pointer approach
        #by the time fast reach to end slow reaches to middle
        #we will keep track of the slow pointer previous using prev node of slow

        #Edge case
        while head is None or head.next is None:
            return None
        
        prev = None
        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = slow.next

        return head
        