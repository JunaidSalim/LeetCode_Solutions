/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution
{
public:
    void flat(TreeNode *node)
    {
        if (!node)
            return;
        TreeNode *left = node->left;
        TreeNode *right = node->right;

        if (left)
        {
            node->right = left;
            node->left = NULL;
            TreeNode *current = node->right;
            while (current->right)
            {
                current = current->right;
            }
            current->right = right;
        }
        flat(node->right);
    }
    void flatten(TreeNode *root)
    {
        flat(root);
    }
};