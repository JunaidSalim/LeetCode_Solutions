/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *temp = head;
        ListNode *current =temp;
        int i=0,size=0;
        while(temp!=NULL)
        {
            temp = temp->next;
            size++;
        }
        temp = head;
        while(i<size-n)
        {
            current =temp;
            temp = temp->next;
            i++;
        }
        if(size-n==0)
        {
            head = head->next;
            delete temp;
            return head;
        }
        current->next = temp->next;
        delete temp;
        return head;
    }
};
