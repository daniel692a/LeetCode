# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None:
            return False
        temp = head
        visited = (10**5)-1
        while temp.next != None:
            if temp.val == visited:
                return True
            else:
                temp.val = visited
            temp = temp.next
        
        return False