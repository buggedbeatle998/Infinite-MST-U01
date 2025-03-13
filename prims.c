#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
#include <time.h>

float times[4] = {0, 0, 0, 0};
const uint32_t num = 10000;
uint32_t heap_size;
const uint16_t heap_width = 2;


typedef struct Node {
    float key;
    uint32_t val;
} Node;


void init_heap(Node **heap);
void heapify(Node **heap, uint32_t index);
Node *extract_root(Node **heap);
void swim_up(Node **heap, uint32_t index);

float prims(float *graph);


int main() {
    srand(time(NULL));
    float *graph = (float *)malloc(num * num * sizeof(float));
    for (uint32_t i = 0; i < num; i++) {
        for (uint32_t j = i + 1; j < num; j++) {
            float weight = (float)rand() / (float)RAND_MAX;
            graph[i * num + j] = weight;
            graph[j * num + i] = weight;
        }
    }
    
    printf("%.6f", prims(graph));
    
    free(graph);
    return 0;
}


float prims(float *graph) {
    Node **heap = (Node **)malloc(num * sizeof(Node *));
    for (uint32_t i = 0; i < num; i++) {
        Node *temp = (Node *)malloc(sizeof(Node));
        temp->key = 2;
        temp->val = i;
        heap[i] = temp;
    }
    init_heap(heap);
    float cost = -2.0f;
    
    for (uint32_t n = 0; n < num; n++) {
        Node *heap_node = extract_root(heap);
        cost += heap_node->key;
        uint32_t val = heap_node->val;
        
        for (uint32_t i = 0; i < heap_size; i++) {
            Node *node = heap[i];
            float new_key = graph[val * num + node->val];
            if (new_key < node->key) {
                node->key = new_key;
                swim_up(heap, i);
            }
        }
    }
    
    printf("Init:    %.6f\nHeapify: %.6f\nExtract: %.6f\nSwim:    %.6f\n", times[0], times[1], times[2], times[3]);
    free(heap);
    return cost;
}


void init_heap(Node **heap) {
    struct timespec ts;
    timespec_get(&ts, TIME_UTC);
    float start = ts.tv_nsec;
    heap_size = num;
    for (int i = (heap_size - 2) / heap_width; i >= 0; i--) {
        heapify(heap, i);
    }
    struct timespec ts2;
    timespec_get(&ts2, TIME_UTC);
    times[0] += (ts2.tv_nsec - start);
}

void heapify(Node **heap, uint32_t index) {
    struct timespec ts;
    timespec_get(&ts, TIME_UTC);
    float start = ts.tv_nsec;
    uint32_t start_index;
    uint32_t end_index;
    Node *min_child;
    Node *parent;

    while ((start_index = index * heap_width + 1) < heap_size && (end_index = (start_index + heap_width < heap_size ? start_index + heap_width : heap_size))) {
        float lowest = 2.0f;
        uint32_t min_child_index = heap_size;
        for (uint32_t i = start_index; i < end_index; i++) {
            if (heap[i]->key < lowest)
                min_child_index = i;
                lowest = heap[i]->key;
        }
        if (min_child_index != heap_size && (min_child = heap[min_child_index])->key < (parent = heap[index])->key) {
            heap[index] = min_child;
            heap[min_child_index] = parent;
        }
        if (min_child_index > heap_size / heap_width) return;
        index = min_child_index;
    }
    struct timespec ts2;
    timespec_get(&ts2, TIME_UTC);
    times[1] += (ts2.tv_nsec - start);
}

Node *extract_root(Node **heap) {
    struct timespec ts;
    timespec_get(&ts, TIME_UTC);
    float start = ts.tv_nsec;
    Node *root = heap[0];
    heap[0] = heap[--heap_size];
    struct timespec ts2;
    timespec_get(&ts2, TIME_UTC);
    times[2] += (ts2.tv_nsec - start);
    heapify(heap, 0);
    return root;
}

void swim_up(Node **heap, uint32_t index) {
    struct timespec ts;
    timespec_get(&ts, TIME_UTC);
    float start = ts.tv_nsec;
    Node *child_node;
    Node *parent_node;
    uint32_t parent;
    while (index && (parent_node = heap[parent = (index - 1) / heap_width])->key > (child_node = heap[index])->key) {
        heap[parent] = child_node;
        heap[index] = parent_node;
        index = parent;
    }
    struct timespec ts2;
    timespec_get(&ts2, TIME_UTC);
    times[3] += (ts2.tv_nsec - start);
}