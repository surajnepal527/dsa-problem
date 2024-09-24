# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return ListNode(val = "")
        head_m = lists[0]
        for i in range(1, len(lists)):
            head_i = lists[i]
            cur_m = head_m
            cur_i = head_i
            dummy = ListNode()
            main_cur = dummy
            while cur_m and cur_i:
                if cur_m.val <= cur_i.val:
                    dummy.next = cur_m
                    cur_m = cur_m.next
                else:
                    dummy.next = cur_i
                    cur_i = cur_i.next
                dummy = dummy.next
            while cur_m:
                dummy.next = cur_m
                cur_m = cur_m.next
                dummy = dummy.next
            while cur_i:
                dummy.next = cur_i
                cur_i = cur_i.next
                dummy = dummy.next
            head_m = main_cur.next
        return head_m
            
        