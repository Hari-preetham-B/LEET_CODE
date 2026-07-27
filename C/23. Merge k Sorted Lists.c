/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
typedef struct ListNode ListNode;
void heap_swap(ListNode** heap, int i, int j) {
    ListNode* temp = heap[i];
    heap[i] = heap[j];
    heap[j] = temp;
}

void heap_push(ListNode** heap, int* heapSize, ListNode* node) {
    heap[*heapSize] = node;
    int i = *heapSize;
    (*heapSize)++;
    while (i > 0) {
        int parent = (i - 1) / 2;
        if (heap[parent]->val > heap[i]->val) {
            heap_swap(heap, parent, i);
            i = parent;
        } else {
            break;
        }
    }
}

ListNode* heap_pop(ListNode** heap, int* heapSize) {
    ListNode* top = heap[0];
    (*heapSize)--;
    heap[0] = heap[*heapSize];
    int i = 0;
    while (1) {
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        int smallest = i;
        if (left < *heapSize && heap[left]->val < heap[smallest]->val) {
            smallest = left;
        }
        if (right < *heapSize && heap[right]->val < heap[smallest]->val) {
            smallest = right;
        }
        if (smallest == i) {
            break;
        }
        heap_swap(heap, i, smallest);
        i = smallest;
    }
    return top;
}

struct ListNode* mergeKLists(struct ListNode** lists, int listsSize) {
    if (listsSize == 0) {
        return NULL;
    }
    ListNode** heap = (ListNode**)malloc(sizeof(ListNode*) * listsSize);
    int heapSize = 0;
    for (int i = 0; i < listsSize; i++) {
        if (lists[i] != NULL) {
            heap_push(heap, &heapSize, lists[i]);
        }
    }
    ListNode dummy;
    dummy.next = NULL;
    ListNode* tail = &dummy;
    while (heapSize > 0) {
        ListNode* smallest = heap_pop(heap, &heapSize);
        tail->next = smallest;
        tail = smallest;
        if (smallest->next != NULL) {
            heap_push(heap, &heapSize, smallest->next);
        }
    }
    tail->next = NULL; 
    free(heap);
    return dummy.next;
}
