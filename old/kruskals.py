from random import random
from sys import argv
from time import perf_counter_ns


class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    def find(self, node):
        while self.parent[node] != node:
            node = self.parent[node]
        return node

    def unite(self, node1, node2):
        node1 = self.find(node1)
        node2 = self.find(node2)
        most = max(node1, node2, key=lambda a: [self.rank[a], a])
        self.parent[min(node1, node2, key=lambda a: [self.rank[a], a])] = most
        if self.rank[node1] == self.rank[node2]:
            self.rank[most] += 1
        # if node1 != node2:
        #     if self.rank[node1] > self.rank[node2]:
        #         self.parent[node2] = node1
        #     if self.rank[node2] > self.rank[node1]:
        #         self.parent[node1] = node2
        #     else:
        #         self.parent[node2] = node1
        #         self.rank[node1] += 1


def kruskal(num, edges):
    times = [0, 0, 0, 0]
    _time0 = perf_counter_ns()
    count: int = 0
    cost: int = 0
    dsu: DSU = DSU(num)
    times[0] += perf_counter_ns() - _time0

    _time0 = perf_counter_ns()
    for (node1, node2), weight in edges:
        _time1 = perf_counter_ns()
        if dsu.find(node1) != dsu.find(node2):
            times[3] += perf_counter_ns() - _time1
            _time1 = perf_counter_ns()
            dsu.unite(node1, node2)
            cost += weight
            times[2] += perf_counter_ns() - _time1

            count += 1
            if count >= num - 1:
                break
    times[1] += perf_counter_ns() - _time0
    print(times)
    return cost


def main(num) -> None:
    sorted_edges = sorted([[{i, j}, random()] for i in range(num) for j in range(i + 1, num)] ,key=lambda a: a[1])
    #print(sorted_edges)
    print(kruskal(num, sorted_edges))


if __name__ == "__main__":
    main(int(argv[1]))