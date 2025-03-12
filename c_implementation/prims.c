#include <stdio.h>
#include "fib_heap.h"
#include <inttypes.h>

const uint32_t num = 10;


float prims(elem **nodes, heap *fib_heap, float *graph) {
    float cost = -2.0f;

    for (uint32_t i = 0; i < num; i++) {
        printf("hi\n");
        data min_node = heap_extract_min(&fib_heap);
        printf("hi\n");
        cost += min_node.key;
        printf("hi\n");
        uint32_t index = *(uint32_t *)min_node.value;
        printf("hi\n");
        nodes[index] = NULL;
        printf("\thi\n");

        for (uint32_t n = 0; n < num; n++) {
            if (nodes[n] != NULL && graph[index * num + n] < nodes[n]->key) {
                //printf("hi");
                heap_decrease_key(&fib_heap, nodes[n], graph[index * num + n]);
            }
        }
        printf("\t\thi\n");
    }

    return cost;
}


int main() {
    float *graph = (float *)malloc(sizeof(float) * num * num);
    for (uint32_t i = 0; i < num; i++) {
        for (uint32_t j = i + 1; j < num; j++) {
            float weight = (float)rand() / (float)RAND_MAX;
            graph[i * num + j] = weight;
            graph[j * num + i] = weight;
        }
    }

    heap *fib_heap = heap_init();
    elem **nodes = (elem **)malloc(sizeof(elem *) * num);
    for (uint32_t i = 0; i < num; i++) {
        uint32_t temp = i;
        nodes[i] = heap_insert(&fib_heap, 2.0f, (void *)&temp);
    }

    printf("%.6f", prims(nodes, fib_heap, graph));

    free(nodes);
    heap_free(&fib_heap);
    free(graph);

    return 0;
}