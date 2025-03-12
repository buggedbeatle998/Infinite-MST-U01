import copy


class Node:
    def __init__(self, key, val, pos):
        self.key = key
        self.val = val
        self.pos = pos
    
    def __lt__(self, other):
        return self.key < other.key
    
    def __gt__(self, other):
        return self.key > other.key
    
    def __le__(self, other):
        return self.key <= other.key
    
    def __ge__(self, other):
        return self.key >= other.key

    def __eq__(self, other):
        return self.key == other.key

    def __ne__(self, other):
        return self.key != other.key


class Dheap(object):
    def __init__(self, k, heap):
        self.heap = copy.deepcopy(heap)
        self.k = k
        if self.heap:
            self.heapify()

    def elements(self):
        """
        Method to return elements of D-ary Heap
        """
        return self.heap

    def length(self):
        """
        Method to return length of D-ary Heap
        """
        return len(self.heap)

    def _get_parent_index(self, child_index):
        """
        Method to find parent node index from child node index
        """
        return (child_index - 1) // self.k

    def heapify(self):
        """
        Method to convert Array into D-ary Heap
        """
        size = self.length()
        for index in reversed(range(
            self._get_parent_index(child_index=(size - 1)) + 1
        )):
            self._heapify(index=index, size=size)

    def get_children(self, parent_index):
        """
        Method to get all the children index from parent index
        """
        children = []
        size = self.length()
        for i in range(self.k):
            child_index = (parent_index * self.k) + (i + 1)
            if child_index < size:
                children.append(self.heap[child_index])
            else:
                break
        return children
    
    def get_children_i(self, parent_index):
        """
        Method to get all the children index from parent index
        """
        children = []
        size = self.length()
        for i in range(self.k):
            child_index = (parent_index * self.k) + (i + 1)
            if child_index < size:
                children.append(child_index)
            else:
                break
        return children

    def swim_up(self, index):
        self._swim_up(index=index)

    def get_root_value(self):
        """
        Return root value of the heap
        """
        return self.heap[0]

    def add_element(self, key, element):
        """
        Brief:
            Method to add element / elements to D-heap
        Args:
            element: Could be a single number of array of numbers
        """
        if isinstance(element, list):
            for _element in element:
                elem = Node(key, _element)
                self.heap.append(elem)
                self.swim_up(self.length() - 1)
        else:
            elem = Node(key, element, self.length())
            self.heap.append(elem)
            self.swim_up(self.length() - 1)
            return elem

    def extract_root(self):
        """
        Remove root element from the heap and return it
        """
        self._swap(0, self.length() - 1)
        result = self.heap.pop()
        self._heapify(index=0, size=self.length())
        return result

    def search_value(self, value):
        """
        Brief:
            Searches the value in heap and returns index
        Args:
            value: The value to be searched in the heap
        Return:
             Returns the index if the value is found otherwise -1
             Note: if same element is present multiple times,
                   first occurring index is returned
        """
        return self._search_value(value, 0)

    def _swap(self, index1, index2):
        """
        Brief:
            Swap two elements in the given heap
        Args:
            index1: Index of the 1st element to be swapped
            index2: Index of the 2nd element to be swapped
        """
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp