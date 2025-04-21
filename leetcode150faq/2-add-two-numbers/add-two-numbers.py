# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        cur = head
        carry = 0
        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            sum = num1+num2+carry
            num = sum%10
            carry = sum//10
            next_node = ListNode(num)
            cur.next = next_node
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if carry:
            next_node = ListNode(carry)
            cur.next = next_node
            cur= cur.next
            
        return head.next    







        