# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        list = []
        node = head
        current = head
        while node:
            if node.val not in list:
                list.append(node.val)
                current = node
            else:
                current.next=node.next    
            node = node.next
        return head
        