# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self,head:Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev

    def getKthNode(self, temp: Optional[ListNode], k: int) -> Optional[ListNode]:
        k-=1
        while k>0 and temp:
            k-=1
            temp = temp.next

        return temp

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        prevLast = None
        while temp:
            kthNode = self.getKthNode(temp,k)
            
            if kthNode is None:
                if prevLast:
                    prevLast.next = temp

                break
            
            nextNode = kthNode.next
            kthNode.next = None

            self.reverseList(temp)

            if temp==head:
                head = kthNode
            else:
                prevLast.next = kthNode
            
            prevLast = temp
            temp = nextNode

        return head
        
        