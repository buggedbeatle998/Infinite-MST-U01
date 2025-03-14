from random import random
from sys import argv
from time import perf_counter_ns
from fib_heap import FibonacciHeap as heap


def prims(num: int, graph: list[list[int]]) -> float:
    fib_heap = heap()
    nodes = [fib_heap.insert(2, i) for i in range(num)]
    cost = -2

    _time = perf_counter_ns()
    for _ in range(num):
        heap_node = fib_heap.extract_min()
        cost += heap_node.key
        nodes[val := heap_node.value] = None
        
        for node in nodes:
            if node:
                fib_heap.decrease_key(node, graph[val][node.value])
    print(perf_counter_ns() - _time)

    return cost


def main(num: int) -> None:
    graph = [[0 for _ in range(num)] for _ in range(num)]
    for i in range(num):
        for j in range(i + 1, num):
            weight = random()
            graph[i][j] = weight
            graph[j][i] = weight
    print(prims(num, graph))


if __name__ == "__main__":
    main(int(argv[1]))