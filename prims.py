from random import random
from sys import argv
from min_d_heap import MinHeap, Node

def prims(num: int, graph: list[list[int]]) -> float:
    d_heap = MinHeap(5, [Node(2, i) for i in range(num)])
    cost = -2

    for _ in range(num):
        heap_node = d_heap.extract_root()
        cost += heap_node.key
        val = heap_node.val
        
        for i, node in enumerate(d_heap.heap):
            if (new_key := graph[val][node.val]) < node.key:
                node.key = new_key
                d_heap.swim_up(i)

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