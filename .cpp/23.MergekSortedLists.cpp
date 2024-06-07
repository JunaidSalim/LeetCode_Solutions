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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        vector<int>temp;
        for(int i =0;i<lists.size();i++)
        {
            while(lists[i])
            {
                temp.push_back(lists[i]->val);
                lists[i]=lists[i]->next;
            }
        }
        sort(rbegin(temp),rend(temp));
        ListNode *res = nullptr;
        for(int i =0;i<temp.size();i++)
        {
            res = new ListNode(temp[i],res);
        }
        return res;
    }
};
