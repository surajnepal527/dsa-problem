# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev_gp = dummy
        cur = head
        while True:
            kthNode = self.getKthNode(prev_gp, k)
            if not kthNode:
                break
            next_node = kthNode.next
            prev = kthNode.next
            cur = prev_gp.next
            while cur and cur != next_node:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            
            tmp = prev_gp.next
            prev_gp.next = kthNode
            prev_gp = tmp

        return dummy.next

    
    def getKthNode(self, head:Optional[ListNode], k:int) -> ListNode:
        cur = head
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur if k == 0 else None
        