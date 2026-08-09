/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
#include <limits.h>
int countGood(struct TreeNode* node, int maxSoFar) {
    if (node == NULL) {
        return 0;
    }
    int count = (node->val >= maxSoFar) ? 1 : 0;
    int newMax = (node->val > maxSoFar) ? node->val : maxSoFar;
    count += countGood(node->left, newMax);
    count += countGood(node->right, newMax);
    return count;
}
int goodNodes(struct TreeNode* root) {
    return countGood(root, INT_MIN);
}
