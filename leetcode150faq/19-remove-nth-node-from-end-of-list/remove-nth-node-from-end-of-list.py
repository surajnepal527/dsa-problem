# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Two pointer approach left and right
        #create the space between two point such that left exactly point to node that is just before node we want to delete
        #just like fast and slow pointer here we are moving right pointer ahead so we know how much we have to move both of theem next
        dummyNode = ListNode(0, head)
        left = right = dummyNode
        for i in range(n+1):
            right = right.next
        while right:
            right = right.next
            left = left.next
        left.next = left.next.next
        return dummyNode.next
        