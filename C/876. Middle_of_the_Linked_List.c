/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
 typedef struct ListNode *node;
struct ListNode* middleNode(struct ListNode* head) {
    node weak=head,strong=head;
    
    while(strong && strong->next){
        weak=weak->next;
        strong=strong->next->next;
    }
    return weak;
}
