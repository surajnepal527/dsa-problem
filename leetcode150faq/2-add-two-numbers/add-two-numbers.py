# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.calNum(l1)
        num2 = self.calNum(l2)
        total_sum = num1+num2
        if total_sum == 0:
            return ListNode(0)
        prev = None
        s_head = None
        while total_sum >0:
            val = total_sum % 10
            total_sum = total_sum // 10
            n_node = ListNode(val)
            if not prev:
                prev = n_node
                s_head = prev
            else:
                prev.next = n_node
            prev = n_node
        
        return s_head

    
    def calNum(self, head:Optional[ListNode]) -> int:
        cur = head
        num = 0
        i = 0
        while cur:
            num += cur.val * (10**i)
            i += 1
            cur = cur.next
        return num
        