# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        
        current = head
        length = 1
        while current.next:
            current = current.next
            length += 1
        current.next = head 
        
        k = k % length
        if k == 0:
            current.next = None 
            return head
        
        steps_to_new_head = length - k
        new_tail = head
        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None  
        
        return new_head