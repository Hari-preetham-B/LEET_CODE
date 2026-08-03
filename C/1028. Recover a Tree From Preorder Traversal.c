#include <string.h>
#include <stdlib.h>
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* recoverFromPreorder(char* S) {
    int len = strlen(S);
    int i = 0;
    struct TreeNode* stack[1001] = {NULL};
    struct TreeNode* root = NULL;
    while (i < len) {
        int depth = 0;
        while (S[i] == '-') {
            depth++;
            i++;
        }
        int val = 0;
        while (i < len && S[i] >= '0' && S[i] <= '9') {
            val = val * 10 + (S[i] - '0');
            i++;
        }
        struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
        node->val = val;
        node->left = NULL;
        node->right = NULL;
        if (depth == 0) {
            root = node;
        } else {
            struct TreeNode* parent = stack[depth - 1];
            if (parent->left == NULL) {
                parent->left = node;
            } else {
                parent->right = node;
            }
        }
        stack[depth] = node;
    }
    return root;
}
