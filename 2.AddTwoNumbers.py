# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        ptr1 = l1
        ptr2 = l2
        
        summ = 0
        carry = 0
        temp = ListNode(0)
        head = temp
        
        while ptr1 or ptr2:
            temp_sum = carry
            if ptr1:
                temp_sum += ptr1.val
                ptr1 = ptr1.next
            if ptr2:
                temp_sum += ptr2.val
                ptr2 = ptr2.next

            summ = temp_sum % 10
            carry = temp_sum // 10
            
            temp.next = ListNode(summ)
            temp = temp.next
        
        if carry > 0:
            temp.next = ListNode(carry)
        
        return head.next