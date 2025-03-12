class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class MinHeap():
    def __init__(self, k, heap):
        self.heap = heap
        self.size = len(heap)
        self.k = k
        self.heapify()

    def heapify(self):
        for index in range((self.size - 2) // self.k, -1, -1):
            self._heapify(index)
    
    def _heapify(self, index):
        while (min_child_index := index * self.k + 1) < self.size and (children := range(min_child_index, min(min_child_index + self.k, self.size))):
            if (min_child := self.heap[min_child_index := min(children, key=lambda a: self.heap[a].key)]).key < (parent := self.heap[index]).key:
                self.heap[index], self.heap[min_child_index] = min_child, parent
            if min_child_index > self.size // self.k:
                return
            index = min_child_index
    
    def extract_root(self):
        self.heap[0], self.heap[self.size - 1] = self.heap[self.size - 1], self.heap[0]
        result = self.heap.pop()
        self.size -= 1
        self._heapify(0)
        return result

    def swim_up(self, index):
        """
        Method to swim up if the children are smaller the root
        Args:
            index: Index of the children
        Example: (4 children heap)
                            1
              2        3         4        5
          6 7 8 9  10 11 12 13  14 15 16 17  18 19 20 21
            In the above heap root will be self.heap[0]
            elements 10, 11 are in respective index 9,10 the parrent node
            will be (children_idex - 1) // self.d = (9 - 1) // 4 => 2
        """
        while index and (parent_node := self.heap[parent := (index - 1) // self.k]).key > (child_node := self.heap[index]).key:
            self.heap[parent], self.heap[index] = child_node, parent_node
            index = parent

    # def search_value(self, value, root):
    #     """
    #     No longer needed but was cool to optimise
    #     """
    #     size = len(self.heap)
    #     to_test = deque([root])
    #     while to_test:
    #         index = to_test.pop()
    #         if (node := self.heap[index]) is value:
    #             return index
    #         if node > value:
    #             continue
    #         index = index * self.k + 1
    #         to_test.extend(range(index, min(index + self.k, size)))
    #     return None