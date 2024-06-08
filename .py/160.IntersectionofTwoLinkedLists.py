# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        node_set = set()
        current = headA
        while current:
            node_set.add(current)
            current = current.next
        current = headB
        while current:
            if current in node_set:
                return current
            current = current.next
        return None