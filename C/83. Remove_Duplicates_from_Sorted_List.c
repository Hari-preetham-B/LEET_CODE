/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
 typedef struct ListNode *node;
struct ListNode* deleteDuplicates(struct ListNode* head) {
    if (head==NULL) return NULL;
    node temp=head;
    while(temp->next!=NULL){
        if (temp->val==temp->next->val){
            node dup=temp->next;
            temp->next=dup->next;
            free(dup);
        }
        else{
            temp=temp->next;
        }
    }
    return head;
}
