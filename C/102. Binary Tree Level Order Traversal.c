/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** levelOrder(struct TreeNode* root, int* returnSize, int** returnColumnSizes) {
    if (root == NULL) {
        *returnSize = 0;
        return NULL;
    }
    int** result = (int**)malloc(sizeof(int*) * 2000);
    *returnColumnSizes = (int*)malloc(sizeof(int) * 2000);
    *returnSize = 0;
    struct TreeNode** queue = (struct TreeNode**)malloc(sizeof(struct TreeNode*) * 2000);
    int front = 0, rear = 0;
    queue[rear++] = root;
    while (front < rear) {
        int levelSize = rear - front;
        int* levelValues = (int*)malloc(sizeof(int) * levelSize);
        for (int i = 0; i < levelSize; i++) {
            struct TreeNode* node = queue[front++];
            levelValues[i] = node->val;
            if (node->left != NULL) {
                queue[rear++] = node->left;
            }
            if (node->right != NULL) {
                queue[rear++] = node->right;
            }
        }
        result[*returnSize] = levelValues;
        (*returnColumnSizes)[*returnSize] = levelSize;
        (*returnSize)++;
    }
    free(queue);
    return result;
}
