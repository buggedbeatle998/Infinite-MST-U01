from random import random
from sys import argv
from time import perf_counter_ns
from fib_heap import FibonacciHeap as heap


def prims(num, graph):
    times = [0, 0, 0, 0]
    _time0 = perf_counter_ns()
    fib_heap = heap()
    for i in range(num):
        fib_heap.insert(2, (i, graph[i]))
    cost = -2
    times[0] += perf_counter_ns() - _time0

    _time0 = perf_counter_ns()
    for i in range(num):
        heap_node = fib_heap.extract_min()
        cost += heap_node.key
        _, adj = heap_node.value
        if fib_heap.root_list:
            while (fib_node:=fib_heap.root_list.right) is not fib_heap.root_list:
                fib_heap.decrease_key(fib_node, adj[fib_node.value[0]])
    times[1] += perf_counter_ns() - _time0
    
    return cost


def main(num) -> None:
    #sorted_edges = sorted([(random(), {i, j}) for i in range(num) for j in range(i + 1, num)])
    graph = [[0 for _ in range(num)] for _ in range(num)]
    for i in range(num):
        for j in range(i + 1, num):
            weight = random()
            graph[i][j] = weight
            graph[j][i] = weight
    # for node in graph:
    #     for edge in node:
    #         print(f"{float(edge):.2f}", end=" ")
    #     print()
    # print(*graph, sep="\n")
    print(prims(num, graph))


if __name__ == "__main__":
    main(int(5))