from random import random
from sys import argv
from time import perf_counter_ns
from fib_heap import FibonacciHeap as heap


def prims(num, graph):
    fib_heap = heap()
    nodes = [None for _ in range(num)]
    for i in range(num):
        nodes[i] = (i, fib_heap.insert(2, (i, graph[i])))
    cost = -2

    for _ in range(num):
        heap_node = fib_heap.extract_min()
        cost += heap_node.key
        _, adj = heap_node.value
        nodes[heap_node.value[0]] = (0, None)
        
        for n, node in nodes:
            if node:
                fib_heap.decrease_key(node, adj[n])

    return cost


def main(num) -> None:
    graph = [[0 for _ in range(num)] for _ in range(num)]
    for i in range(num):
        for j in range(i + 1, num):
            weight = random()
            graph[i][j] = weight
            graph[j][i] = weight
    print(prims(num, graph))


if __name__ == "__main__":
    main(int(argv[1]))