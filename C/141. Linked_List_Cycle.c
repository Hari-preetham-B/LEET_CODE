/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    struct ListNode*weak=head,*strong=head;
    while(strong && strong->next){
        weak=weak->next;
        strong=strong->next->next;
        if(weak==strong)
            return true;
    }
    return false;

    
}
