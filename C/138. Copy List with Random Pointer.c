/**
 * Definition for a Node.
 * struct Node {
 *     int val;
 *     struct Node *next;
 *     struct Node *random;
 * };
 */

struct Node* copyRandomList(struct Node* head) {
    if (head == NULL) {
        return NULL;
    }

    struct Node* curr = head;
    while (curr != NULL) {
        struct Node* copy = (struct Node*)malloc(sizeof(struct Node));
        copy->val = curr->val;
        copy->next = curr->next;
        copy->random = NULL;  
        curr->next = copy;
        curr = copy->next;
    }

    curr = head;
    while (curr != NULL) {
        struct Node* copy = curr->next;
        if (curr->random != NULL) {
            copy->random = curr->random->next;
        }
        curr = copy->next;
    }

    struct Node* copyHead = head->next;
    curr = head;
    struct Node* copyCurr = copyHead;

    while (curr != NULL) {
        curr->next = curr->next->next;
        if (copyCurr->next != NULL) {
            copyCurr->next = copyCurr->next->next;
        }
        curr = curr->next;
        copyCurr = copyCurr->next;
    }

    return copyHead;
}
