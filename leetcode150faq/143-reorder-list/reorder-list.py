# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #find the total length
        n, cur, headm = 0, head, head
        while cur:
            cur = cur.next
            n += 1
        mid = n//2

        #lets find the mid point
        m = 0
        n_cur = head
        prev_one = None
        while m <= mid:
            prev_one = n_cur
            n_cur = n_cur.next
            m += 1

        n_mid = n_cur
        prev_one.next = None
        #let revers it 
        prev_two = None
        while n_mid:
            n_mid_next = n_mid.next
            n_mid.next = prev_two
            prev_two = n_mid
            n_mid = n_mid_next
        # now let switch the pointer as per questions
        headn = prev_two
        cur_main = headm
        cur_new = headn
        while cur_main and cur_new:
            next_main = cur_main.next
            next_new = cur_new.next
            cur_main.next = cur_new
            cur_new.next = next_main
            cur_main = next_main
            cur_new = next_new    
        
        




