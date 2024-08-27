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
class Solution
{
public:
    ListNode *reverseList(ListNode *head)
    {
        ListNode *current = head;
        ListNode *prev = NULL;
        while (current)
        {
            ListNode *temp = current->next;
            current->next = prev;
            prev = current;
            current = temp;
        }
        return prev;
    }
    ListNode *getKthNode(ListNode *temp, int k)
    {
        k -= 1;
        while (k > 0 && temp)
        {
            k -= 1;
            temp = temp->next;
        }
        return temp;
    }

    ListNode *reverseKGroup(ListNode *head, int k)
    {
        ListNode *temp = head;
        ListNode *prevLast = NULL;
        while (temp)
        {
            ListNode *kthNode = getKthNode(temp, k);

            if (kthNode == NULL)
            {
                if (prevLast)
                {
                    prevLast->next = temp;
                }
                break;
            }

            ListNode *nextNode = kthNode->next;
            kthNode->next = NULL;

            reverseList(temp);

            if (temp == head)
            {
                head = kthNode;
            }
            else
            {
                prevLast->next = kthNode;
            }

            prevLast = temp;
            temp = nextNode;
        }
        return head;
    }
};