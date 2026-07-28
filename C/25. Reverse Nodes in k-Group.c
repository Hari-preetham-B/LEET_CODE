/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* reverseKGroup(struct ListNode* head, int k) {
    if (head == NULL || k == 1) {
        return head;
    }

    struct ListNode dummy;
    dummy.next = head;
    struct ListNode* groupPrev = &dummy;

    while (1) {
        
        struct ListNode* node = groupPrev;
        for (int i = 0; i < k; i++) {
            node = node->next;
            if (node == NULL) {
                return dummy.next;  
            }
        }

        struct ListNode* groupNext = node->next;  

        struct ListNode* prev = groupNext;
        struct ListNode* curr = groupPrev->next;

        while (curr != groupNext) {
            struct ListNode* temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }

        struct ListNode* newGroupPrev = groupPrev->next; 
        groupPrev->next = node;             
        groupPrev = newGroupPrev;           
    }
}
