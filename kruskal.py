from random import random, randrange


class Graph:
    def __init__(self, n):
        self.edges = dict([[(i, j), random()] for i in range(n) for j in range(i + 1, n)])
    

class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    def find(self, node):
        return node if self.parent[node] == node else self.find(self.parent[node])
    
    def unite(self, node1, node2):
        node1 = self.find(node1)
        node2 = self.find(node2)
        if node1 != node2:
            if self.rank[node1] > self.rank[node2]:
                self.parent[node2] = node1
            if self.rank[node2] > self.rank[node1]:
                self.parent[node1] = node2
            else:
                self.parent[node2] = node1
                self.rank[node1] += 1


def kruskal(edges):
    num = len(edges)
    count: int = 0
    cost: int = 0
    dsu: DSU = DSU(num)

    for (node1, node2), weight in edges:
        if dsu.find(node1) != dsu.find(node2):
            dsu.unite(node1, node2)
            cost += weight

            count += 1
            if count >= num - 1:
                break
    return cost


def main(num) -> None:
    graph: Graph = Graph(num)
    sorted_edges = sorted(list(graph.edges.items()),key=lambda a: a[1])
    #print(sorted_edges)
    print(kruskal(sorted_edges))


if __name__ == "__main__":
    for i in range(10):
        main(1000)