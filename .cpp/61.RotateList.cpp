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
    ListNode *rotateRight(ListNode *head, int k)
    {
        if (!head || k == 0)
            return head;

        ListNode *current = head;
        int length = 1;
        while (current->next)
        {
            current = current->next;
            length += 1;
        }
        current->next = head;

        k = k % length;
        if (k == 0)
        {
            current->next = nullptr;
            return head;
        }

        int steps_to_new_head = length - k;
        ListNode *new_tail = head;
        for (int i = 0; i < steps_to_new_head - 1; ++i)
        {
            new_tail = new_tail->next;
        }

        ListNode *new_head = new_tail->next;
        new_tail->next = nullptr;

        return new_head;
    }
};