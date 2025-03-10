from random import random
from sys import argv
from time import perf_counter_ns
from fib_heap import FibonacciHeap as heap


def prims(num, graph):
    times = [0, 0, 0, 0]
    _time0 = perf_counter_ns()
    fib_heap = heap()
    for i in range(num):
        fib_heap.insert(graph[i][0], i)
    visited = [False for _ in range(num)]
    cheapest = [2 for _ in range(num)]
    cost = -2
    times[0] += perf_counter_ns() - _time0

    _time0 = perf_counter_ns()
    
    for _ in range(num - 1):
        node = fib_heap.extract_min().value
        cost += cheapest[node]
        for fib_node in fib_heap.iterate(fib_heap.root_list):
            fib_heap.decrease_key(fib_node, graph[fib_node.value][node])
        visited[node] = True
        for edge, weight in enumerate(graph[node]):
            if not visited[edge] and weight < cheapest[edge]:
                cheapest[edge] = weight
    times[1] += perf_counter_ns() - _time0
    
    # print(*best_edge)
    # print(*cheapest)
    return cost

    #return cost


def main(num) -> None:
    sorted_edges = sorted([(random(), {i, j}) for i in range(num) for j in range(i + 1, num)])
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
    main(int(argv[1]))