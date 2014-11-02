struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
class Solution {
public:
    TreeNode* dfs(TreeNode* root) {
        if (root->left == NULL && root->right == NULL) {
            return root;
        } else {
            TreeNode* left = root->left;
            TreeNode* right = root->right;
            if (left != NULL) {
                root->right = left;
                TreeNode* head = dfs(left);
                if (right != NULL) {
                    head->right = right;
                    return dfs(right);
                }
                return head;
            } else {
                return dfs(right);
            }
        }
    }
    void flatten(TreeNode *root) {
        if (root != NULL) {
            TreeNode* h = root;
            dfs(h);
        }
    }
};
