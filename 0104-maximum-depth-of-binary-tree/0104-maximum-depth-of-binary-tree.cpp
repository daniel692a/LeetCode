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
class Solution {
public:
    int maxDepth(TreeNode* root) {
        int max_depth = 0;
        DFS(root, max_depth, 1);
        return max_depth;
    }
    void DFS(TreeNode* root, int &maxd, int step){
        if(!root){
            step--;
            maxd = max(maxd, step);
            return;
        }
        DFS(root->left, maxd, step+1);
        DFS(root->right, maxd, step+1);
    }
};