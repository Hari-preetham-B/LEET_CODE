/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
 typedef struct ListNode *node;
void reorderList(struct ListNode* head) {
    if (head ==NULL || head->next ==NULL){
        return;
    }
    node slow=head,fast=head;
    while(fast->next!=NULL && fast->next->next!=NULL){
        slow=slow->next;
        fast=fast->next->next;
    }
    node sec=slow->next;
    slow->next=NULL;
    node prev=NULL;
    node curr=sec;
    while(curr!=NULL){
        node temp=curr->next;
        curr->next=prev;
        prev=curr;
        curr=temp;
    }
    sec=prev;
    node first=head;
    while(sec!=NULL){
        node fn=first->next;
        node sn=sec->next;
        first->next=sec;
        sec->next=fn;
        first=fn;
        sec=sn;
    }

}
