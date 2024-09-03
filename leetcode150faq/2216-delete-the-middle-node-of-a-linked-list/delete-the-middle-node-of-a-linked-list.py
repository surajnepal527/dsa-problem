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
        #let take care of edge cases
        if head is None:
            return None

        #Lets find the length of the Linked List in first iteration
        temp = head
        length = 0
        while temp is not None:
            length += 1
            temp = temp.next
        
        if length == 1:
            return None
        #find the middle index
        middle_index = length // 2

        cur = head
        cur_index = 0
        while cur is not None and cur_index < middle_index - 1:
            cur = cur.next
            cur_index += 1

        
        cur.next = cur.next.next
        return head
        

