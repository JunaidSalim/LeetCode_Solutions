/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution
{
public:
    Node *copyRandomList(Node *head)
    {
        if (!head)
            return nullptr;

        Node *temp = head;

        // Creating a new list in between
        while (temp)
        {
            Node *copyNode = new Node(temp->val);
            copyNode->next = temp->next;
            temp->next = copyNode;
            temp = copyNode->next;
        }

        temp = head;

        // Placing random pointers
        while (temp)
        {
            if (temp->random)
            {
                temp->next->random = temp->random->next;
            }
            temp = temp->next->next;
        }

        temp = head;

        // Removing connections
        Node *dummyNode = new Node(-1);
        Node *res = dummyNode;

        while (temp)
        {
            res->next = temp->next;
            res = res->next;
            temp->next = temp->next->next;
            temp = temp->next;
        }

        return dummyNode->next;
    }
};