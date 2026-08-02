/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int checkHeight(struct TreeNode* node) {
    if (node == NULL) {
        return 0;
    }

    int leftHeight = checkHeight(node->left);
    if (leftHeight == -1) {
        return -1;  // left subtree already unbalanced, short-circuit
    }

    int rightHeight = checkHeight(node->right);
    if (rightHeight == -1) {
        return -1;  // right subtree already unbalanced, short-circuit
    }

    int diff = leftHeight - rightHeight;
    if (diff > 1 || diff < -1) {
        return -1;  // imbalance found at this node
    }

    return 1 + (leftHeight > rightHeight ? leftHeight : rightHeight);
}

bool isBalanced(struct TreeNode* root) {
    return checkHeight(root) != -1;
}
