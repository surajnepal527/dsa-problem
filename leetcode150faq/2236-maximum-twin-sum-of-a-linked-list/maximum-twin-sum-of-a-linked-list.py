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
        slow , fast = head , head
        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
            

        max_sum = -1
        while prev and slow:
            max_sum = max(max_sum, prev.val + slow.val)
            prev = prev.next
            slow = slow.next
        
        return max_sum
 

            
            
