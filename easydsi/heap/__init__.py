# Import the libraries
import heapq

class MinHeap():

    root = []

    def __init__(self, data = []):
        self.root = data
        heapq.heapify(self.root)

    def add(self, element):
        heapq.heappush(self.root, element)

    def remove(self):
        return heapq.heappop(self.root)

    def get_largest(self, count = 1):
        return heapq.nlargest( count, self.root)

    def get_smallest(self, count = 1):
        return heapq.nsmallest( count, self.root)

    def display(self):
        print(list(self.root))

    def get_elements(self):
        return list(self.root)

class MaxHeap(MinHeap):

    root = []

    def __init__(self, data):
        self.root = [-i for i in data]
        heapq.heapify(self.root)

    def add(self, element):
        heapq.heappush(self.root, -element)

    def remove(self):
        return -heapq.heappop(self.root)

    def get_largest(self, count = 1):
        li = heapq.nlargest( count, self.root)
        li = [-i for i in li]

    def get_smallest(self, count = 1):
        li = heapq.nsmallest( count, self.root)
        li = [-i for i in li]

    def display(self):
        li = list(self.root)
        li = [-i for i in li]
        print(li)

    def get_elements(self):
        li = list(self.root)
        li = [-i for i in li]
        return li

def heap(data = []):
    return MinHeap(data)

def min_heap(data = []):
    return MinHeap(data)

def max_heap(data = []):
    return MaxHeap(data)