# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1:
            return list2
        if not list2:
            return list1
        head3 = None
        if list1.val <= list2.val:
            head3 = ListNode(list1.val, None)
            list1 = list1.next
        else:
            head3 = ListNode(list2.val, None)
            list2 = list2.next
        
        cur3 = head3
        while list1 and list2:
            cur = None
            if list1.val <= list2.val:
                cur = ListNode(list1.val, None)
                list1 = list1.next
            else:
                cur = ListNode(list2.val, None)
                list2 = list2.next
            cur3.next = cur
            cur3 = cur3.next
        
        while list1:
            cur = ListNode(list1.val, None)
            list1 = list1.next
            cur3.next = cur
            cur3 = cur3.next
        while list2:
            cur = ListNode(list2.val, None)
            list2 = list2.next
            cur3.next = cur
            cur3 = cur3.next
        
        return head3





















        