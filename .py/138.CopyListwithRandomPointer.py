"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head

        # Creating a new List In Between
        while temp:
            copyNode = Node(temp.val)
            copyNode.next = temp.next
            temp.next = copyNode
            temp = temp.next.next
        

        temp = head
        # Placing Random Pointers
        while temp:
            temp2 = temp.next
            if temp.random:
                temp2.random = temp.random.next
            else:
                temp2.random = None
            temp = temp.next.next

        temp = head

        # Removing Connections
        dummyNode = Node(-1)
        res = dummyNode
        while temp:
            res.next = temp.next
            res = res.next

            temp.next = temp.next.next
            temp = temp.next

        return dummyNode.next