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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummy=new ListNode();
        ListNode *temp=dummy;
        ListNode* current;
        ListNode *t1= l1;
        ListNode *t2=l2;
        int carry =0;
        if(!l1)
        {
            return l2;
        }
        if(!l2)
        {
            return l1;
        }
        while(t1!=NULL && t2!=NULL)
        {
            int sum = t1->val + t2->val+carry;
            if(sum>9)
            {
                ListNode* newnode=new ListNode((sum%10));
                temp->next=newnode;
                temp=temp->next;
               carry =1;
            }
            else
            {
                ListNode* newnode=new ListNode((sum%10));
                temp->next=newnode;
                temp=temp->next;
                carry=0;
            }
            t1 = t1->next;
            t2=t2->next;
        }
        while(t1)
        {
            int sum = t1->val + carry;
            if(sum>9)
            {
                ListNode* newnode=new ListNode((sum%10));
                temp->next=newnode;
                temp=temp->next;
                carry =1;
            }
            else
            {
                ListNode* newnode=new ListNode((sum%10));
                temp->next=newnode;
                temp=temp->next;
                carry=0;
            }
            t1=t1->next;
        }
        while(t2)
        {
            int sum = t2->val + carry;
            if(sum>9)
            {
                ListNode* newnode=new ListNode((sum%10));
                temp->next=newnode;
                temp=temp->next;
                carry =1;
            }
            else
            {
                ListNode* newnode=new ListNode((sum%10));
                temp->next=newnode;
                temp=temp->next;
                carry=0;
            }
            t2=t2->next;
        }
        if(carry!=0)
        {
            ListNode* newnode=new ListNode(carry);
            temp->next=newnode;
            temp=temp->next;
        }
        ListNode *head = dummy->next;
        delete dummy;
        return head;
    }
};
