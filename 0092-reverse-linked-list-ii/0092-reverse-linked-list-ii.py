# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], l: int, r: int) -> Optional[ListNode]:
        if not head or l==r:
            return head
        
        dummy = ListNode(0, head)
        prev = dummy

        for _ in range(l-1):
            prev = prev.next

        current = prev.next

        for _ in range(r-l):
            next_node = current.next
            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return dummy.next
