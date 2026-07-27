#include <stdlib.h>

#define HASH_SIZE 10007

typedef struct DNode {
    int key;
    int value;
    struct DNode* prev;
    struct DNode* next;
    struct DNode* hash_next;  
} DNode;

typedef struct {
    int capacity;
    int size;
    DNode* head;  
    DNode* tail; 
    DNode* buckets[HASH_SIZE];
} LRUCache;

int hash_func(int key) {
    long k = key;
    if (k < 0) k = -k;
    return (int)(k % HASH_SIZE);
}

LRUCache* lRUCacheCreate(int capacity) {
    LRUCache* cache = (LRUCache*)malloc(sizeof(LRUCache));
    cache->capacity = capacity;
    cache->size = 0;

    cache->head = (DNode*)malloc(sizeof(DNode));
    cache->tail = (DNode*)malloc(sizeof(DNode));
    cache->head->next = cache->tail;
    cache->tail->prev = cache->head;
    cache->head->prev = NULL;
    cache->tail->next = NULL;

    for (int i = 0; i < HASH_SIZE; i++) {
        cache->buckets[i] = NULL;
    }

    return cache;
}
DNode* find_node(LRUCache* cache, int key) {
    int idx = hash_func(key);
    DNode* node = cache->buckets[idx];
    while (node != NULL) {
        if (node->key == key) return node;
        node = node->hash_next;
    }
    return NULL;
}

void hash_insert(LRUCache* cache, DNode* node) {
    int idx = hash_func(node->key);
    node->hash_next = cache->buckets[idx];
    cache->buckets[idx] = node;
}

void hash_remove(LRUCache* cache, int key) {
    int idx = hash_func(key);
    DNode* node = cache->buckets[idx];
    DNode* prevNode = NULL;
    while (node != NULL) {
        if (node->key == key) {
            if (prevNode == NULL) {
                cache->buckets[idx] = node->hash_next;
            } else {
                prevNode->hash_next = node->hash_next;
            }
            return;
        }
        prevNode = node;
        node = node->hash_next;
    }
}
void list_remove(DNode* node) {
    node->prev->next = node->next;
    node->next->prev = node->prev;
}
void list_insert_front(LRUCache* cache, DNode* node) {
    node->next = cache->head->next;
    node->prev = cache->head;
    cache->head->next->prev = node;
    cache->head->next = node;
}

int lRUCacheGet(LRUCache* obj, int key) {
    DNode* node = find_node(obj, key);
    if (node == NULL) {
        return -1;
    }
    list_remove(node);
    list_insert_front(obj, node);
    return node->value;
}

void lRUCachePut(LRUCache* obj, int key, int value) {
    DNode* node = find_node(obj, key);

    if (node != NULL) {
        node->value = value;
        list_remove(node);
        list_insert_front(obj, node);
        return;
    }

    DNode* newNode = (DNode*)malloc(sizeof(DNode));
    newNode->key = key;
    newNode->value = value;
    list_insert_front(obj, newNode);
    hash_insert(obj, newNode);
    obj->size++;

    if (obj->size > obj->capacity) {
        DNode* lru = obj->tail->prev;
        list_remove(lru);
        hash_remove(obj, lru->key);
        free(lru);
        obj->size--;
    }
}

void lRUCacheFree(LRUCache* obj) {
    DNode* curr = obj->head;
    while (curr != NULL) {
        DNode* next = curr->next;
        free(curr);
        curr = next;
    }
    free(obj);
}
