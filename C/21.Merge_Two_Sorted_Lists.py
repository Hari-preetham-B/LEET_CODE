/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
 typedef struct ListNode *node;
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    node head;
    if(list1==NULL){
            return list2;
        }
        else if(list2==NULL){
            return list1;
        }
    struct ListNode* temp1=list1;
    struct ListNode* temp2=list2;
    if(list1->val>list2->val){
        head=list2;
        temp2=list2->next;
        }
        else{
            head=list1;
            temp1=list1->next;
        }
        struct ListNode* temp=head;
        while(temp1!=NULL && temp2!=NULL){
            if(temp1->val<temp2->val){
                temp->next=temp1;
                temp1=temp1->next;
            }
            else{
                temp->next=temp2;
                temp2=temp2->next;
            }
            temp=temp->next;
        }
        if(temp1!=NULL){
            temp->next=temp1;
        }
        else if(temp2!=NULL){
            temp->next=temp2;
        }
        return head;
}
