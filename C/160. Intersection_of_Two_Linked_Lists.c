/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
typedef struct ListNode *node;
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    if(headA==NULL || headB==NULL)
        return NULL;
    node tempa = headA;
    node tempb = headB;
    while(tempa!=tempb){
        if(tempa==NULL)
            tempa = headB;
        else
            tempa = tempa->next;
            
        if(tempb==NULL)
            tempb = headA;
        else
            tempb = tempb->next;
    }

    return tempa;
}
