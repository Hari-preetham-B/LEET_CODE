/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int height(struct TreeNode* node, int* diameter) {
    if (node == NULL) {
        return 0;
    }

    int leftHeight = height(node->left, diameter);
    int rightHeight = height(node->right, diameter);

    int pathThroughNode = leftHeight + rightHeight;
    if (pathThroughNode > *diameter) {
        *diameter = pathThroughNode;
    }

    return 1 + (leftHeight > rightHeight ? leftHeight : rightHeight);
}

int diameterOfBinaryTree(struct TreeNode* root) {
    int diameter = 0;
    height(root, &diameter);
    return diameter;
}
